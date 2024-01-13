# Demonstrates modulo operator
x = int(input("What's x? "))

if x % 2 == 0:
    print("Even")
else:
    print("Odd")


# Demonstrates a function that returns a bool
def main():
    x = int(input("What's x? "))
    if is_even(x):
        print("Even")
    else:
        print("Odd")


def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False


main()


# Demonstrates conditional expressions (ternary operators)
def main2():
    x = int(input("What's x? "))
    if is_even2(x):
        print("Even")
    else:
        print("Odd")


def is_even2(n):
    return True if n % 2 == 0 else False


main2()


# Demonstrates returning the value of a Boolean expression
def main3():
    x = int(input("What's x? "))
    if is_even3(x):
        print("Even")
    else:
        print("Odd")


def is_even3(n):
    return n % 2 == 0


main3()
