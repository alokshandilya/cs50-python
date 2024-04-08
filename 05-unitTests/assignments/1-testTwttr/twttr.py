def main():
    str = input("Enter Message : ")
    result = shorten(str)
    print(result)


def shorten(word):
    remove = "AEIOUaeiou"
    result = ""

    for _ in range(len(word)):
        if not word[_] in remove:
            result = result + word[_]
    return f"{result}"


if __name__ == "__main__":
    main()
