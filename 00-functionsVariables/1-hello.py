# Demonstrates a function with a positional argument
print("hello, world")

# Demonstrates a function with a positional argument and a return value
name = input("What's your name? ")
print("hello,")
print(name)

# Demonstrates concatenation of strings
name = input("What's your name? ")
print("hello, " + name)

# Demonstrates a function with two positional arguments
name = input("What's your name? ")
print("hello,", name)

# Demonstrates a function with a positional argument and a named argument
name = input("What's your name? ")
print("hello, ", end="")
print(name)

# Demonstrates a format string
name = input("What's your name? ")
print(f"hello, {name}")

# Demonstrates str functions
# strip() is a built-in string method that removes whitespaces
# capitalize() is a built-in string method that capitalize first letter
# title() is a built-in string method that capitalize first letter of each word
name = input("What's your name? ")
name = name.strip().title()
print(f"hello, {name}")

# split() split a string into a list of substrings based on specified separator
# By default, splits the string using spaces as the separator
# you can specify a different separator within the parentheses of the split()
name = input("What's your name? ")
first, last = name.split(" ")
print(f"hello, {first}")


# Demonstrates defining a function without parameters
def hello():
    print("hello")


name = input("What's your name? ")
hello()
print(name)


# Demonstrates defining a function with a parameter
def hello2(to):
    print("hello,", to)


name = input("What's your name? ")
hello2(name)
print("#############################")


# Demonstrates defining a function with a parameter with a default value
def hello3(par="world"):
    print("hello,", par)


hello3()
name = input("What's your name? ")
hello3(name)


# Demonstrates defining a main function
def main():
    name = input("What's your name? ")
    hello4(name)


def hello4(to="world"):
    print("hello,", to)


main()
