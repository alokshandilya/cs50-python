def main():
    percentage = fraction_to_percentage()
    if percentage == 100 or percentage == 99:
        print("F")
    elif percentage == 0 or percentage == 1:
        print("E")
    else:
        print(str(percentage) + "%")


def fraction_to_percentage():
    while True:
        try:
            fraction = input("Fraction: ").strip()
            a, b = fraction.split("/")
            # int("11.1") gives ValueError
            # int(float("11.1")) gives no error
            percent = round((int(a) / int(b)), 2) * 100
        except (ValueError, ZeroDivisionError):
            pass
        else:
            if int(percent) <= 100:
                return int(percent)


main()
