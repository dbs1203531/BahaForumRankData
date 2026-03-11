import time
import logging
import requests
from scraper.parse import parse_boards_from_html

logger = logging.getLogger(__name__)

SSR_BASE = "https://forum.gamer.com.tw/"

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/124.0.0.0 Safari/537.36"
    ),
    "Referer": "https://forum.gamer.com.tw/",
    "Accept-Language": "zh-TW,zh;q=0.9,en;q=0.8",
}
REQUEST_DELAY = 1.5
MAX_RETRIES = 3


def _get_with_retry(url: str, params: dict, timeout: int) -> requests.Response:
    for attempt in range(1, MAX_RETRIES + 1):
        try:
            resp = requests.get(url, params=params, headers=HEADERS, timeout=timeout)
            resp.raise_for_status()
            return resp
        except requests.RequestException as exc:
            logger.warning("Attempt %d/%d failed for %s: %s", attempt, MAX_RETRIES, url, exc)
            if attempt < MAX_RETRIES:
                time.sleep(REQUEST_DELAY * attempt)
    raise RuntimeError(f"All {MAX_RETRIES} attempts failed for {url}")


def collect_category(c: int, pages_needed: int) -> list[dict]:
    """Fetch `pages_needed` pages for category `c` via SSR, returning deduplicated boards sorted by rank."""
    all_boards: dict[int, dict] = {}

    for page in range(1, pages_needed + 1):
        logger.info("Fetching c=%s page=%s", c, page)
        resp = _get_with_retry(SSR_BASE, {"c": c, "page": page}, timeout=20)
        items = parse_boards_from_html(resp.text)

        for board in items:
            bsn = board.get("bsn")
            if bsn and bsn not in all_boards:
                all_boards[bsn] = board

        if page < pages_needed:
            time.sleep(REQUEST_DELAY)

    result = sorted(all_boards.values(), key=lambda b: b.get("rank") or 9999)
    return result
