import csv
import sys
from tabulate import tabulate


def main():
    if len(sys.argv) > 2:
        sys.exit("Too many arguments")
    elif len(sys.argv) < 2:
        sys.exit("Too less arguments")
    elif not sys.argv[1].endswith(".csv"):
        sys.exit("Not a CSV file")
    else:
        print_table(sys.argv[1])


def print_table(file):
    table = []

    try:
        with open(file, "r") as f:
            reader = csv.reader(f)
            for row in reader:
                table.append(row)
    except FileNotFoundError:
        sys.exit("File not found")
    else:
        print(tabulate(table, headers="firstrow", tablefmt="grid"))


if __name__ == "__main__":
    main()
