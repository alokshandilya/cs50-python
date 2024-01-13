def convert(str):
    str = str.replace(":)", "🙂")
    str = str.replace(":(", "🙁")
    return str


def main():
    a = input()
    str = convert(a)
    print(str, end="")


main()
