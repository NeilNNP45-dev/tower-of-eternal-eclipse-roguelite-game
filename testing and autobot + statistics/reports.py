import json

STATS_FILE = "statistics.json"
REPORT_FILE = "report.txt"


def generate_report():
    try:
        with open(STATS_FILE, "r") as file:
            runs = json.load(file)

    except (FileNotFoundError, json.JSONDecodeError):
        print("No statistics found.")
        return

    if len(runs) == 0:
        print("No statistics found.")
        return

    total_runs = len(runs)

    total_resets = 0
    total_level = 0
    total_floor = 0
    total_exp = 0

    total_crits = 0
    total_misses = 0

    total_normal = 0
    total_strong = 0
    total_special = 0

    highest_floor = 0
    highest_level = 0
    lowest_resets = None

    for run in runs:

        total_resets += run["resets"]
        total_level += run["level"]
        total_floor += run["floor"]
        total_exp += run["exp"]

        total_crits += run["crits"]
        total_misses += run["misses"]

        total_normal += run["normal_attacks"]
        total_strong += run["strong_attacks"]
        total_special += run["special_attacks"]

        if run["floor"] > highest_floor:
            highest_floor = run["floor"]

        if run["level"] > highest_level:
            highest_level = run["level"]

        if lowest_resets is None or run["resets"] < lowest_resets:
            lowest_resets = run["resets"]

    average_resets = total_resets / total_runs
    average_level = total_level / total_runs
    average_floor = total_floor / total_runs
    average_exp = total_exp / total_runs

    total_non_special = total_normal + total_strong
    total_attacks = total_non_special + total_special

    if total_non_special > 0:
        crit_percent = (total_crits / total_non_special) * 100
    else:
        crit_percent = 0

    if total_special > 0:
        miss_percent = (total_misses / total_special) * 100
    else:
        miss_percent = 0

    normal_percent = (total_normal / total_attacks) * 100
    strong_percent = (total_strong / total_attacks) * 100
    special_percent = (total_special / total_attacks) * 100

    with open(REPORT_FILE, "w") as report:

        report.write("===== TOWER OF ETERNAL ECLIPSE =====\n")
        report.write("========== AUTOBOT REPORT ==========\n\n")

        report.write(f"Total Simulations : {total_runs}\n\n")

        report.write("----- Average Statistics -----\n")
        report.write(f"Average Resets : {average_resets:.2f}\n")
        report.write(f"Average Level  : {average_level:.2f}\n")
        report.write(f"Average Floor  : {average_floor:.2f}\n")
        report.write(f"Average EXP    : {average_exp:.2f}\n\n")

        report.write("----- Best Results -----\n")
        report.write(f"Highest Floor : {highest_floor}\n")
        report.write(f"Highest Level : {highest_level}\n")
        report.write(f"Lowest Resets : {lowest_resets}\n\n")

        report.write("----- Combat Statistics -----\n")
        report.write(f"Total Attacks        : {total_attacks}\n")
        report.write(f"Normal Attacks       : {total_normal}\n")
        report.write(f"Strong Attacks       : {total_strong}\n")
        report.write(f"Special Attacks      : {total_special}\n\n")

        report.write(f"Normal Attack Usage  : {normal_percent:.2f}%\n")
        report.write(f"Strong Attack Usage  : {strong_percent:.2f}%\n")
        report.write(f"Special Attack Usage : {special_percent:.2f}%\n\n")

        report.write(f"Total Crits          : {total_crits}\n")
        report.write(f"Critical Hit Rate    : {crit_percent:.2f}%\n\n")

        report.write(f"Total Misses         : {total_misses}\n")
        report.write(f"Special Miss Rate    : {miss_percent:.2f}%\n")
generate_report()
print("Report generated successfully!")