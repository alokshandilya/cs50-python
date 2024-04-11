import sys
import csv


def main():
    file_name_old = sys.argv[1]
    file_name_new = sys.argv[2]

    if not len(sys.argv) == 3:
        sys.exit("too many or less arguments, 2 needed")
    else:
        with open(file_name_old, "r") as f_old:
            with open(file_name_new, "w") as f_new:
                reader = csv.DictReader(f_old)
                writer = csv.DictWriter(f_new, fieldnames=["first", "last", "house"])
                writer.writeheader()
                for row in reader:
                    last_name, first_name = row["name"].split(",")
                    writer.writerow(
                        {
                            "first": first_name.lstrip(),
                            "last": last_name,
                            "house": row["house"],
                        }
                    )


if __name__ == "__main__":
    main()
