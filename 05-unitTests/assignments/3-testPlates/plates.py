def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if len(s) < 2 or not s[0].isalpha() or not s[1].isalpha():
        return False

    if len(s) < 2 or len(s) > 6:
        return False

    if not s.isalnum():
        return False

    seen_digit = False
    for c in s:
        if c.isdigit():
            if c == "0" and not seen_digit:
                return False
            seen_digit = True

        elif seen_digit:
            return False

    return True


if __name__ == "__main__":
    main()
