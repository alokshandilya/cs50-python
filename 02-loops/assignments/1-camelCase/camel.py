def main():
    camel_case = input("Enter in camelCase : ")
    snake_case = camel_to_snake(camel_case)
    print(snake_case)


def camel_to_snake(str):
    result = ""
    for _ in range(len(str)):
        if str[_] in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            result = result + "_" + str[_].lower()
        else:
            result += str[_]
    return result


main()
