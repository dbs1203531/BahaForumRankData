import csv
import logging
from datetime import date
from pathlib import Path

logger = logging.getLogger(__name__)

DATA_DIR = Path("data")
FIELDNAMES = ["rank", "title", "popularity", "article", "bsn"]


def save_csv(slug: str, boards: list[dict]) -> Path:
    """Write boards to data/{date}_{slug}.csv with utf-8-sig encoding."""
    DATA_DIR.mkdir(exist_ok=True)
    today = date.today().isoformat()
    filepath = DATA_DIR / f"{today}_{slug}.csv"

    with filepath.open("w", newline="", encoding="utf-8-sig") as f:
        writer = csv.DictWriter(f, fieldnames=FIELDNAMES, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(boards)

    logger.info("Saved %d rows to %s", len(boards), filepath)
    return filepath
