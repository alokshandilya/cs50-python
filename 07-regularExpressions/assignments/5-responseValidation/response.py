from validators import email


def main():
    print(validate(input("Enter email address : ")))


def validate(s):
    if email(s) == True:
        return f"Valid"
    else:
        return f"Invalid"


if __name__ == "__main__":
    main()
