import json
import logging
from datetime import date
from pathlib import Path

logger = logging.getLogger(__name__)

DATA_DIR = Path("data")
LATEST_DIR = DATA_DIR / "latest"
DOCS_DATA_DIR = Path("docs") / "data"
SOURCE_URL = "https://forum.gamer.com.tw/"
BOARD_URL_TEMPLATE = "https://forum.gamer.com.tw/B.php?bsn={bsn}"


def _normalize_board(board: dict, slug: str, label: str) -> dict:
    bsn = board.get("bsn")
    return {
        "rank": board.get("rank"),
        "title": (board.get("title") or "").strip(),
        "popularity": board.get("popularity"),
        "article": board.get("article"),
        "bsn": bsn,
        "board_url": BOARD_URL_TEMPLATE.format(bsn=bsn),
        "category_slug": slug,
        "category_label": label,
    }


def _write_json(path: Path, payload: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        json.dumps(payload, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )


def save_json(results: dict[str, list[dict]], categories: dict[str, dict]) -> None:
    """Persist combined and per-category JSON feeds for the embed site."""
    today = date.today().isoformat()
    combined = {
        "generated_at": today,
        "source_url": SOURCE_URL,
        "categories": {},
    }

    for slug, cfg in categories.items():
        label = cfg["label"]
        boards = [_normalize_board(board, slug, label) for board in results.get(slug, [])]
        category_payload = {
            "generated_at": today,
            "source_url": SOURCE_URL,
            "category": {
                "slug": slug,
                "label": label,
                "board_count": len(boards),
            },
            "boards": boards,
        }
        combined["categories"][slug] = category_payload["category"] | {"boards": boards}

        _write_json(LATEST_DIR / f"{slug}.json", category_payload)
        _write_json(DOCS_DATA_DIR / f"{slug}.json", category_payload)

    _write_json(DATA_DIR / "latest.json", combined)
    _write_json(DOCS_DATA_DIR / "latest.json", combined)
    logger.info("Saved JSON feeds to %s and %s", DATA_DIR, DOCS_DATA_DIR)
