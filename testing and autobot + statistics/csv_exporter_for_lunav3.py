import json
import csv
from pathlib import Path


BASE_DIR = Path(__file__).parent

STATS_FILE = BASE_DIR / "statistics.json"
CSV_FILE = BASE_DIR / "training_data_simulations.csv"


def average(values):
    """
    Returns the average of a list.
    If the list is empty, returns 0.
    """
    if not values:
        return 0

    return sum(values) / len(values)


def export_simulation_csv():

    try:
        with open(STATS_FILE, "r") as file:
            runs = json.load(file)

    except (FileNotFoundError, json.JSONDecodeError):
        print("No statistics found.")
        return


    with open(CSV_FILE, "w", newline="") as csvfile:

        writer = csv.writer(csvfile)


        # Luna V3 dataset columns
        writer.writerow([
            "Resets",
            "Level",
            "EXP",
            "Highest Death Floor",
            "Killer Type",
            "Average Killer Health Remaining",
            "Average Killer Health Percent",
            "Total Damage Dealt",
            "Total Damage Taken",
            "Crits",
            "Misses",
            "Normal Attacks",
            "Strong Attacks",
            "Special Attacks"
        ])


        for run in runs:

            death_floors = run["death floor"]

            killer_types = run["killer type"]


            # Successful run:
            # no deaths happened, so use final floor reached
            if death_floors:

                highest_death_floor = max(death_floors)

            else:

                highest_death_floor = run["floor"]


            # If there were deaths, use final killer.
            # If player won, there is no killer.
            if killer_types:

                final_killer_type = killer_types[-1]

            else:

                final_killer_type = "No killer"


            writer.writerow([

                # Target variable
                run["resets"],


                # Progression
                run["level"],
                run["exp"],


                # Death information
                highest_death_floor,


                # Enemy information
                final_killer_type,


                # Boss/enemy survival information
                average(run["killer health remaining"]),
                average(run["killer health percent"]),


                # Whole simulation combat performance
                sum(run["total damage dealt"]),
                sum(run["total damage taken"]),


                # Combat behaviour
                run["crits"],
                run["misses"],
                run["normal_attacks"],
                run["strong_attacks"],
                run["special_attacks"]

            ])


    print(f"Simulation CSV exported successfully to '{CSV_FILE}'")


if __name__ == "__main__":
    export_simulation_csv()