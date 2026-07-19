import json
import csv
from pathlib import Path

BASE_DIR = Path(__file__).parent

STATS_FILE = BASE_DIR / "statistics.json"
CSV_FILE = BASE_DIR / "training_data.csv"


def export_csv():
    try:
        with open(STATS_FILE, "r") as file:
            runs = json.load(file)

    except (FileNotFoundError, json.JSONDecodeError):
        print("No statistics found.")
        return

    with open(CSV_FILE, "w", newline="") as csvfile:

        writer = csv.writer(csvfile)

        writer.writerow([
            "Class",
            "Death Floor",
            "Battle Turns",
            "Killer",
            "Killer Type",
            "Killer Health Remaining",
            "Killer Health Percent",
            "Damage Dealt",
            "Damage Taken",
            "Resets",
            "Level",
            "Floor Reached",
            "EXP",
            "Crits",
            "Misses",
            "Normal Attacks",
            "Strong Attacks",
            "Special Attacks"
        ])

        for run in runs:
            deaths = len(run["death floor"])

            for i in range(deaths):
                writer.writerow([
                    run["class"],
                    run["death floor"][i],
                    run["turns"][i],
                    run["killer"][i],
                    run["killer type"][i],
                    run["killer health remaining"][i],
                    run["killer health percent"][i],
                    run["total damage dealt"][i],
                    run["total damage taken"][i],
                    run["resets"],
                    run["level"],
                    run["floor"],
                    run["exp"],
                    run["crits"],
                    run["misses"],
                    run["normal_attacks"],
                    run["strong_attacks"],
                    run["special_attacks"]
                ])

    print(f"CSV exported successfully to '{CSV_FILE}'")


if __name__ == "__main__":
    export_csv()