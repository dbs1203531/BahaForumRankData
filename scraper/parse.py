import re
import json
import logging

logger = logging.getLogger(__name__)

# Captures the string argument inside self.__next_f.push([1,"..."])
# (?:[^"\\]|\\.)*  matches any char except quote/backslash, or a backslash-escape sequence
PUSH_PATTERN = re.compile(
    r'self\.__next_f\.push\(\[1,"((?:[^"\\]|\\.)*)"\]\)',
    re.DOTALL,
)

# Strip Next.js chunk-ID prefix like "12:" before the JSON body
CHUNK_PREFIX = re.compile(r'^\d+:')


def _collect_boards(obj, seen_bsn: set, results: list) -> None:
    """Recursively walk parsed JSON to find all board objects (have both bsn and rank)."""
    if isinstance(obj, dict):
        if "bsn" in obj and "rank" in obj:
            bsn = obj["bsn"]
            if bsn not in seen_bsn:
                seen_bsn.add(bsn)
                results.append({
                    "rank":       obj.get("rank"),
                    "title":      (obj.get("title") or "").strip(),
                    "popularity": obj.get("popularity"),
                    "article":    obj.get("article"),
                    "bsn":        bsn,
                })
        else:
            for v in obj.values():
                _collect_boards(v, seen_bsn, results)
    elif isinstance(obj, list):
        for item in obj:
            _collect_boards(item, seen_bsn, results)


def parse_boards_from_html(html: str) -> list[dict]:
    """Extract board entries from Next.js SSR HTML.

    The data lives inside JSON-encoded strings in self.__next_f.push([1,"..."]) calls.
    Quotes inside are escaped (\\"), so we must unescape the outer string first,
    strip the chunk-ID prefix, then JSON-parse the inner payload.
    """
    boards: list[dict] = []
    seen_bsn: set = set()

    for push_match in PUSH_PATTERN.finditer(html):
        raw = push_match.group(1)

        # Unescape the JSON string value
        try:
            content: str = json.loads('"' + raw + '"')
        except json.JSONDecodeError:
            continue

        if "bsn" not in content:
            continue

        # Strip Next.js chunk prefix (e.g. "12:")
        content = CHUNK_PREFIX.sub("", content, count=1)

        try:
            data = json.loads(content)
        except json.JSONDecodeError:
            logger.warning("Failed to JSON-parse push content (first 120 chars): %s", content[:120])
            continue

        _collect_boards(data, seen_bsn, boards)

    boards.sort(key=lambda b: b.get("rank") or 9999)

    if not boards:
        logger.warning("No boards found — page structure may have changed.")

    return boards
