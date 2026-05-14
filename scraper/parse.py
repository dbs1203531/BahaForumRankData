import json
import logging
import re

from bs4 import BeautifulSoup

logger = logging.getLogger(__name__)

# Captures the string argument inside self.__next_f.push([1,"..."])
# (?:[^"\\]|\\.)*  matches any char except quote/backslash, or a backslash-escape sequence
PUSH_PATTERN = re.compile(
    r'self\.__next_f\.push\(\[1,"((?:[^"\\]|\\.)*)"\]\)',
    re.DOTALL,
)

# Strip Next.js chunk-ID prefix like "12:" before the JSON body
CHUNK_PREFIX = re.compile(r'^\d+:')
BSN_PATTERN = re.compile(r'B\.php\?bsn=(\d+)')


def _to_int(value) -> int | None:
    if value is None:
        return None

    text = str(value).replace(",", "").strip()
    if not text.isdigit():
        return None

    return int(text)


def _parse_boards_from_cards(html: str) -> list[dict]:
    """Extract board entries from the current SSR card markup."""
    soup = BeautifulSoup(html, "html.parser")
    boards: list[dict] = []
    seen_bsn: set[int] = set()

    for card in soup.select("[data-rank]"):
        rank = _to_int(card.get("data-rank"))
        if rank is None:
            continue

        board_link = card.find("a", href=BSN_PATTERN)
        if not board_link:
            continue

        bsn_match = BSN_PATTERN.search(board_link.get("href", ""))
        if not bsn_match:
            continue

        bsn = int(bsn_match.group(1))
        if bsn in seen_bsn:
            continue

        title_node = card.find("h3")
        title = title_node.get_text(strip=True) if title_node else ""
        if not title:
            image_node = board_link.find("img", alt=True)
            title = image_node.get("alt", "").strip() if image_node else ""

        metric_spans = [
            span for span in card.find_all("span")
            if span.find("data", attrs={"value": True})
        ]

        popularity = None
        article = None
        if metric_spans:
            popularity_node = metric_spans[0].find("data", attrs={"value": True})
            popularity = _to_int(popularity_node.get("value"))
        if len(metric_spans) > 1:
            article_node = metric_spans[1].find("data", attrs={"value": True})
            article = _to_int(article_node.get("value"))

        seen_bsn.add(bsn)
        boards.append({
            "rank": rank,
            "title": title,
            "popularity": popularity,
            "article": article,
            "bsn": bsn,
        })

    boards.sort(key=lambda b: b.get("rank") or 9999)
    return boards


def _collect_boards(obj, seen_bsn: set, results: list) -> None:
    """Recursively walk parsed JSON to find all board objects (have both bsn and rank)."""
    if isinstance(obj, dict):
        if "bsn" in obj and "rank" in obj:
            bsn = obj["bsn"]
            if bsn not in seen_bsn:
                seen_bsn.add(bsn)
                results.append({
                    "rank": obj.get("rank"),
                    "title": (obj.get("title") or "").strip(),
                    "popularity": obj.get("popularity"),
                    "article": obj.get("article"),
                    "bsn": bsn,
                })
        else:
            for v in obj.values():
                _collect_boards(v, seen_bsn, results)
    elif isinstance(obj, list):
        for item in obj:
            _collect_boards(item, seen_bsn, results)


def _parse_boards_from_next_chunks(html: str) -> list[dict]:
    """Extract board entries from the legacy Next.js flight payload."""
    boards: list[dict] = []
    seen_bsn: set = set()

    for push_match in PUSH_PATTERN.finditer(html):
        raw = push_match.group(1)

        try:
            content: str = json.loads('"' + raw + '"')
        except json.JSONDecodeError:
            continue

        if "bsn" not in content:
            continue

        content = CHUNK_PREFIX.sub("", content, count=1)

        try:
            data = json.loads(content)
        except json.JSONDecodeError:
            logger.warning("Failed to JSON-parse push content (first 120 chars): %s", content[:120])
            continue

        _collect_boards(data, seen_bsn, boards)

    boards.sort(key=lambda b: b.get("rank") or 9999)
    return boards


def parse_boards_from_html(html: str) -> list[dict]:
    """Extract board entries from Baha forum ranking HTML."""
    boards = _parse_boards_from_cards(html)

    if not boards:
        boards = _parse_boards_from_next_chunks(html)

    if not boards:
        logger.warning("No boards found - page structure may have changed.")

    return boards
