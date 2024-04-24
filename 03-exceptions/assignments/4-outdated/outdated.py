def main():
    mm, dd, yyyy = get_date()
    print(f"{int(yyyy):04}-{int(mm):02}-{int(dd):02}")


def get_date():
    months = [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December",
    ]
    while True:
        try:
            date = input("Date: ").strip()
            if "/" in date:
                mm, dd, yyyy = date.split("/")
            elif "," in date:
                mm, dd, yyyy = date.split(" ")
                dd = dd.removesuffix(",")
                mm = months.index(mm) + 1

            if int(mm) > 12 or int(dd) > 31:
                raise ValueError

        except (ValueError, KeyError, UnboundLocalError):
            pass
        else:
            return mm, dd, yyyy


main()
