import re
import json
import logging

logger = logging.getLogger(__name__)

BOARD_PATTERN = re.compile(
    r'\{"bsn":\d+,"title":"[^"]+","imageUrl":"[^"]*","popularity":\d+,'
    r'"article":\d+,[^}]*"rank":\d+[^}]*\}',
    re.DOTALL,
)


def parse_boards_from_html(html: str) -> list[dict]:
    """Extract board entries from Next.js SSR HTML."""
    matches = BOARD_PATTERN.findall(html)
    boards = []
    seen_bsn = set()

    for raw in matches:
        try:
            board = json.loads(raw)
        except json.JSONDecodeError:
            logger.warning("Failed to parse board JSON: %s", raw[:120])
            continue

        bsn = board.get("bsn")
        if bsn in seen_bsn:
            continue
        seen_bsn.add(bsn)

        boards.append({
            "rank":       board.get("rank"),
            "title":      board.get("title"),
            "popularity": board.get("popularity"),
            "article":    board.get("article"),
            "bsn":        bsn,
        })

    boards.sort(key=lambda b: b["rank"] or 9999)
    return boards
