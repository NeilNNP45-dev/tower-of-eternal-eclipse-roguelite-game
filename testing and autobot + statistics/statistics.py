import json

FILE_NAME = "statistics.json"


def save_run(run_data):
    try:
        with open(FILE_NAME, "r") as file:
            data = json.load(file)

    except (FileNotFoundError, json.JSONDecodeError):
        data = []

    data.append(run_data)

    with open(FILE_NAME, "w") as file:
        json.dump(data, file, indent=4)