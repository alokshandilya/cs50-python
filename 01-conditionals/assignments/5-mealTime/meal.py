def main():
    time = input("Enter time : ")
    time = convert(time)

    if 7.00 <= time <= 8.00:
        print("breakfast time")
    elif 12.00 <= time <= 13.00:
        print("lunch time")
    elif 18.00 <= time <= 19.00:
        print("dinner time")


def convert(time):
    hour, min = time.split(":")
    min = int(min)
    min, min_new = str(min / 60).split(".")
    time_str = hour + "." + min_new
    return float(time_str)


if __name__ == "__main__":
    main()
