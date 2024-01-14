def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    # All vanity plates must start with at least two letters
    if len(s) < 2 or not s[0].isalpha() or not s[1].isalpha():
        return False

    if len(s) < 2 or len(s) > 6:
        return False

    # No periods, spaces, or punctuation marks are allowed
    if not s.isalnum():
        return False

    # Numbers cannot be used in the middle of a plate; they must come at end
    # The first number used cannot be a ‘0’.
    # means : once a number comes, rest all should be numbers
    # also, input with all letter should be True (CSM etc.)
    seen_digit = False
    for c in s:
        if c.isdigit():
            if c == "0" and not seen_digit:
                return False
            seen_digit = True

        elif seen_digit:
            return False

    return True


main()
