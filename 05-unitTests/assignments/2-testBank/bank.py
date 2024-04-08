def main():
    greeting = input("Greeting : ")
    bank_fine = value(greeting)
    print(f"${bank_fine}")


def value(greeting):
    greeting = greeting.strip().casefold()
    if greeting.startswith("hello"):
        return 0
    elif greeting.startswith("h"):
        return 20
    else:
        return 100


if __name__ == "__main__":
    main()
