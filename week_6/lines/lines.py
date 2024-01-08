import sys
import argparse

def count_non_empty_lines(filename):
    """
    Count non-empty lines in a file, excluding lines starting with '#' (comments).

    Args:
        filename (str): The name of the file to process.

    Returns:
        int: The number of non-empty lines.
    """
    try:
        with open(filename) as file:
            return sum(1 for line in file if line.strip() and not line.lstrip().startswith("#"))
    except FileNotFoundError:
        sys.exit(f"Error: File '{filename}' does not exist.")

def parse_arguments():
    """
    Parse command-line arguments using argparse.

    Returns:
        argparse.Namespace: The parsed arguments.
    """
    parser = argparse.ArgumentParser(description="Count non-empty lines in a Python file.")
    parser.add_argument("filename", help="The name of the Python file to process.")
    return parser.parse_args()

def main():
    # Parse command-line arguments
    args = parse_arguments()

    # Check if the file has a '.py' extension
    if not args.filename.endswith(".py"):
        sys.exit("Error: Invalid file extension. Please provide a Python file.")

    # Count non-empty lines in the specified file
    lines_count = count_non_empty_lines(args.filename)

    # Print the result
    print(f"The number of non-empty lines in '{args.filename}' is: {lines_count}")

if __name__ == "__main__":
    main()
