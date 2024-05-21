import csv

def write_dict_array_csv(csv_file_name, data, fieldnames):
    with open(csv_file_name, "w", newline="") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for row in data:
            writer.writerow(row)


