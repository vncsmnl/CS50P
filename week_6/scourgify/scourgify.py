import csv
import sys
import argparse

def process_csv(input_file, output_file):
    try:
        with open(input_file) as input, open(output_file, "w", newline="") as output:
            reader = csv.DictReader(input)
            writer = csv.DictWriter(output, fieldnames=["first", "last", "house"])
            writer.writeheader()

            for row in reader:
                last_name, first_name = row["name"].strip().split(", ")
                writer.writerow(
                    {"first": first_name, "last": last_name, "house": row["house"]}
                )

    except FileNotFoundError:
        sys.exit(f"Error: File '{input_file}' does not exist.")
    except ValueError as ve:
        sys.exit(f"Error: {ve}")

def main():
    parser = argparse.ArgumentParser(description="Process CSV file.")
    parser.add_argument("input_file", help="Input CSV file")
    parser.add_argument("output_file", help="Output CSV file")

    args = parser.parse_args()

    if not args.input_file.endswith(".csv"):
        sys.exit("Error: Input file must have a .csv extension.")

    process_csv(args.input_file, args.output_file)

if __name__ == "__main__":
    main()
