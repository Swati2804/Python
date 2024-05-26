import csv

file_path = "example.csv"

try:
    with open(file_path, "r", newline="") as csvfile:
        csvreader = csv.reader(csvfile)

        # Skip the header row if you don't want it in the data
        # next(csvreader)

        for row in csvreader:
            # Each row is a list representing a line in the CSV file
            name, age, city = row
            print(f"Name: {name}, Age: {age}, City: {city}")

except FileNotFoundError:
    print(f"File '{file_path}' not found.")
except Exception as e:
    print(f"Error occurred: {e}")
