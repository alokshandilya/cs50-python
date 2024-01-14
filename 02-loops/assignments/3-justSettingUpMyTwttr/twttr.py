def main():
    str = input("Enter Message : ")
    remove = "AEIOUaeiou"
    result = ""

    for _ in range(len(str)):
        if not str[_] in remove:
            result = result + str[_]
    print(result)


main()
