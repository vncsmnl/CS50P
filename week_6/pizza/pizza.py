from tabulate import tabulate
import csv
import sys
import os

def display_csv_table(csv_file):
    try:
        with open(csv_file, newline='') as file:
            data = csv.DictReader(file)
            print(tabulate(data, headers="keys", tablefmt="grid"))
    except FileNotFoundError:
        sys.exit(f"Error: File '{csv_file}' not found.")
    except Exception as e:
        sys.exit(f"Error: An unexpected error occurred - {e}")

def main():
    if len(sys.argv) != 2 or not sys.argv[1].endswith(".csv"):
        sys.exit("Usage: python script.py <input_file.csv>")

    csv_file = sys.argv[1]

    if not os.path.isfile(csv_file):
        sys.exit(f"Error: File '{csv_file}' not found.")

    display_csv_table(csv_file)

if __name__ == "__main__":
    main()
