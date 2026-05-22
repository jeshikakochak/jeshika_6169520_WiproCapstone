import csv


def get_csv_data(file_path):

    data = []

    with open(file_path, newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for row in reader:
            data.append(row["product"])

    return data