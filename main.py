import csv
import itertools
import math
import os
import time
from brute_force import brute_force
from optimized import optimized





# Define the directory where the CSV files are located
print("Brute force or optimized? \n 1: Brute force \n 2: Optimized \n -> ")
algorithm_choice = int(input())
directory = "./.csv/"
if algorithm_choice == 1:
    directory += "brute_force/"
elif algorithm_choice == 2:
    directory += "optimized/"

# Get a list of all CSV files in the directory
csv_files_names = [
    directory + filename
    for filename in os.listdir(directory)
    if filename.endswith(".csv")
]
# Read the CSV files and store the data in a list of dictionaries
data = []
for file_name in csv_files_names:
    with open(file_name, "r") as file:
        reader = csv.DictReader(file, delimiter=",")
        for i, row in enumerate(reader):
            row["price"] = float(row["price"])
            row["profit"] = 1 + float(row["profit"]) / 100
            row["benefit"] = row["price"] * row["profit"]
            data.append(row)


if algorithm_choice == 1:
    brute_force(data)
elif algorithm_choice == 2:
    optimized(data)
