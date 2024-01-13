def calculateExp(str, x, y):
    if "+" in str:
        print(x + y)
    elif "-" in str:
        print(x - y)
    elif "*" in str:
        print(x * y)
    elif "/" in str:
        print(x / y)
    else:
        print("wrong operator")


def main():
    exp = input("enter arithmetic expresssion : ").strip()
    x, y, z = exp.split(" ")
    x = float(x)
    z = float(z)
    calculateExp(exp, x, z)
    del y


main()
