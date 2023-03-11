import csv
import os
from brute_force import brute_force, brute_force_PQ
from greedy import greedy
from dynamic import print_dynamic_results


class Action:
    def __init__(self, name, price, profit):
        self.name = name
        self.price = float(price)
        self.profit = float(profit)

    def __str__(self):
        return f"{self.name} {self.price:.2f}€ {self.profit:.2f}% "

    def __repr__(self):
        return f"{self.name} {self.price:.2f}€ {self.profit:.2f}% "


# Define the directory where the CSV files are located
print("Brute force or optimized? \n 1: Brute force \n 2: Optimized \n 3: Dynamic \n ")
algorithm_choice = int(input("->"))
directory = "./.csv/"
# Get a list of all CSV files in the directory
csv_files_names = [
    filename for filename in os.listdir(directory) if filename.endswith(".csv")
]

# Print the list of CSV file names with indices
print("Choose a CSV file by entering its index:")
for i, csv_file_name in enumerate(csv_files_names):
    print(f"{i}: {csv_file_name}")

# Prompt the user for the CSV file index
csv_file_index = int(input("->"))
csv_file_name = csv_files_names[csv_file_index]
csv_file_path = os.path.join(directory, csv_file_name)

# Read the CSV file and store the data in a list of Action objects
data = []
with open(csv_file_path, "r") as file:
    reader = csv.DictReader(file, delimiter=",")
    for i, row in enumerate(reader):
        action = Action(row["name"], row["price"], row["profit"])
        data.append(action)

# Call the chosen algorithm on the data
if algorithm_choice == 1:
    brute_force(data)
elif algorithm_choice == 2:
    greedy(data)
elif algorithm_choice == 3:
    print_dynamic_results(data)
