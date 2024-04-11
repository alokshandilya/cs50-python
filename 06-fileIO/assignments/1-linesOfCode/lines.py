import sys


def main():
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    else:
        if not sys.argv[1].endswith(".py"):
            sys.exit("Not a Python file")
        line_count = count_lines(sys.argv[1])
        print(line_count)


def count_lines(file_name):
    try:
        with open(file_name, "r") as file:
            lines = file.readlines()
            count = 0
            for line in lines:
                if line.lstrip().startswith("#"):
                    continue
                elif line.lstrip() == "" or line == "\n":
                    continue
                else:
                    count += 1
            return count
    except FileNotFoundError:
        sys.exit("File does not exist")


if __name__ == "__main__":
    main()
