# Gets a number from the user
x = int(input("What's x? "))
print(f"x is {x}")

# Catches a ValueError
try:
    # x is assigned to int value only, if no ValueError
    x = int(input("What's x? "))
    # will continue only if no ValueError
    print(f"x is {x}")
except ValueError:
    print("x is not an integer")

# Demonstrates a NameError
try:
    # no assignment, x = {ValueError}
    x = int(input("What's x? "))
except ValueError:
    print("x is not an integer")
# NameError if input value is not int, because x doesn't get assigned
print(f"x is {x}")

# Demonstrates else
try:
    x = int(input("What's x? "))
except ValueError:
    print("x is not an integer")
else:
    # if no ValueError then only execute
    # if ValueError then don't execute
    print(f"x is {x}")

# Adds a loop
while True:
    try:
        x = int(input("What's x? "))
    except ValueError:
        print("x is not an integer")
    else:
        break

print(f"x is {x}")


# Adds functions, uses break and return
def main():
    x = get_int()
    print(f"x is {x}")


def get_int():
    while True:
        try:
            x = int(input("What's x? "))
        except ValueError:
            print("x is not an integer")
        else:
            break
    return x


main()


# Removes break
def main2():
    x = get_int2()
    print(f"x is {x}")


def get_int2():
    while True:
        try:
            x = int(input("What's x? "))
        except ValueError:
            print("x is not an integer")
        else:
            return x


main2()


# Removes else
def main3():
    x = get_int3()
    print(f"x is {x}")


def get_int3():
    while True:
        try:
            return int(input("What's x? "))
        except ValueError:
            print("x is not an integer")


main3()


# Adds pass
def main4():
    x = get_int4()
    print(f"x is {x}")


def get_int4():
    while True:
        try:
            return int(input("What's x? "))
        except ValueError:
            # no message (not an integer)
            pass


main4()


# Adds prompt
def main5():
    x = get_int5("What's x? ")
    print(f"x is {x}")


def get_int5(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            pass


main5()
