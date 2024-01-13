# Prints a column of bricks
print("#")
print("#")
print("#")

print("-------")

# Prints column of bricks using a loop
for _ in range(3):
    print("#")

print("-------")


# Prints column of bricks using a function with a loop
def main():
    print_column(3)


def print_column(height):
    for _ in range(height):
        print("#")


main()

print("-------")


# Prints column of bricks using a function with str multiplication
def main2():
    print_column2(3)


def print_column2(height):
    print("#\n" * height, end="")


main2()

print("-------")


# Prints row of coins using a function with str multiplication
def main3():
    print_row3(4)


def print_row3(width):
    print("?" * width)


main3()

print("-------")


# Prints square of bricks using a function with nested loops
def main4():
    print_square4(3)


def print_square4(size):
    for i in range(size):
        for j in range(size):
            print("#", end="")
        print()


main4()

print("-------")


# Prints square of bricks using a function with a loop and str multiplication
def main5():
    print_square5(3)


def print_square5(size):
    for _ in range(size):
        print("#" * size)


main5()

print("-------")


# Prints square of bricks using a function with a loop and str multiplication
def main6():
    print_square6(3)


def print_square6(size):
    for _ in range(size):
        print_row6(size)


def print_row6(width):
    print("#" * width)


main6()
