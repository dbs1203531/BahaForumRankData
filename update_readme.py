import re
import logging
from datetime import date
from pathlib import Path

logger = logging.getLogger(__name__)

README_PATH = Path("README.md")

MARKER_MAP = {
    "mobile":    ("MOBILE_TABLE_START",    "MOBILE_TABLE_END"),
    "pc":        ("PC_TABLE_START",        "PC_TABLE_END"),
    "lifestyle": ("LIFESTYLE_TABLE_START", "LIFESTYLE_TABLE_END"),
}


def _build_table(boards: list[dict], top_n: int) -> str:
    today = date.today().isoformat()
    lines = [
        f"_更新時間: {today}_",
        "",
        "| 排名 | 專版名稱 | 人氣 | 昨日文章 |",
        "|------|----------|------|----------|",
    ]
    for board in boards[:top_n]:
        rank       = board.get("rank", "")
        title      = board.get("title", "")
        popularity = board.get("popularity", "")
        article    = board.get("article", "")
        lines.append(f"| {rank} | {title} | {popularity} | {article} |")
    return "\n".join(lines) + "\n"


def update_readme(results: dict[str, list[dict]], top_n: int) -> None:
    """Replace table content between markers for each category in README.md."""
    content = README_PATH.read_text(encoding="utf-8")
    replacement_count = 0

    for slug, (start_marker, end_marker) in MARKER_MAP.items():
        if slug not in results:
            logger.warning("No data for slug '%s', skipping README update.", slug)
            continue

        table = _build_table(results[slug], top_n)
        pattern = re.compile(
            rf"(<!-- {re.escape(start_marker)} -->).*?(<!-- {re.escape(end_marker)} -->)",
            re.DOTALL,
        )

        new_content, n = pattern.subn(
            rf"\1\n{table}\2",
            content,
        )

        if n == 0:
            raise ValueError(
                f"Marker '<!-- {start_marker} -->' not found in README.md. "
                "Please ensure all three marker pairs are present."
            )

        content = new_content
        replacement_count += 1
        logger.info("Updated README table for '%s'.", slug)

    if replacement_count != len(MARKER_MAP):
        raise ValueError(
            f"Expected {len(MARKER_MAP)} table replacements, but only performed {replacement_count}."
        )

    README_PATH.write_text(content, encoding="utf-8")
    logger.info("README.md updated successfully.")
