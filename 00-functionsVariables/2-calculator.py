# Demonstrates addition
x = 1
y = 2
z = x + y
print(z)

# Demonstrates (unintended) concatenation of strings
# Prompt user for two integers
x = input("What's x? ")
y = input("What's y? ")
z = x + y
print(z)

# Demonstrates conversion from str to int
x = input("What's x? ")
y = input("What's y? ")
z = int(x) + int(y)
print(z)

# Demonstrates nesting of function calls
x = int(input("What's x? "))
y = int(input("What's y? "))
z = x + y
print(z)

# Demonstrates conversion of str to float
x = float(input("What's x? "))
y = float(input("What's y? "))
z = x + y
print(z)

# Demonstrates rounding to nearest int
x = float(input("What's x? "))
y = float(input("What's y? "))
z = round(x + y)
print(z)

# Demonstrates fewer variables
x = float(input("What's x? "))
y = float(input("What's y? "))
print(round(x + y))

# Demonstrates formatting with commas
x = float(input("What's x? "))
y = float(input("What's y? "))
z = round(x + y)
# format a number with commas as thousand separators
print(f"{z:,}")  # like 1,234,567,890

# Demonstrates division
# division with int also returns float
x = float(input("What's x? "))
y = float(input("What's y? "))
z = x / y
print(z)

# Demonstrates rounding after the decimal point
x = float(input("What's x? "))
y = float(input("What's y? "))
z = round(x / y, 2)
print(z)

# Demonstrates formatting after the decimal place
x = int(input("What's x? "))
y = int(input("What's y? "))
z = x / y
print(f"{z:.2f}")


# Demonstrates defining a function with a return value
def main():
    x = int(input("What's x? "))
    print("x squared is", square(x))


def square(n):
    return n * n
    # return n ** 2
    # return pow(n, 2)


main()
