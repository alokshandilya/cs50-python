def valid_or_not(str):
    str = str.strip().casefold()
    if str.startswith("hello"):
        print("$0")
    elif str.startswith("h"):
        print("$20")
    else:
        print("$100")


def main():
    greeting = input("Greeting : ")
    valid_or_not(greeting)


main()
