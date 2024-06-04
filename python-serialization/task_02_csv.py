#!/usr/bin/python3
"""This is the task_02_csv
Module
"""
import csv
import json


def convert_csv_to_json(csvFile):
    """A func csv to json
    Args:
        csvFile: csv to conver
        data.json: json file to write to
    """

    # create dict
    data = []

    try:
        with open(csvFile) as csvF:
            csvReader = csv.DictReader(csvF)
            for row in csvReader:
                data.append(row)
    except FileNotFoundError:
        return False
    try:
        with open("data.json", "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4)
    except Exception:
        return False
    return True
