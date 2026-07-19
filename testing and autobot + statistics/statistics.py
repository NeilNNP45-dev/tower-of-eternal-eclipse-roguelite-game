import json
from pathlib import Path

BASE_DIR = Path(__file__).parent
STATS_FILE = BASE_DIR / "statistics.json"


def save_run(run_data):
    try:
        with open(STATS_FILE, "r") as file:
            data = json.load(file)

    except (FileNotFoundError, json.JSONDecodeError):
        data = []

    data.append(run_data)

    with open(STATS_FILE, "w") as file:
        json.dump(data, file, indent=4)