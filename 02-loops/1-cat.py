# Demonstrates multiple (identical) function calls
print("meow")
print("meow")
print("meow")

print("#######")

# Demonstrates a while loop, counting down
i = 3
while i != 0:
    print("meow")
    i = i - 1

print("#######")

# Demonstrates a while loop, counting up from 1
i = 1
while i <= 3:
    print("meow")
    i = i + 1

print("#######")

# Demonstrates a while loop, counting up from 0
i = 0
while i < 3:
    print("meow")
    i = i + 1

print("#######")

# Demonstrates (more succinct) incrementation
i = 0
while i < 3:
    print("meow")
    i += 1

print("#######")

# Demonstrates a for loop, using a list
for i in [0, 1, 2]:
    print("meow")

print("#######")

# Demonstrates a for loop, using range
for i in range(3):
    print("meow")

print("#######")

# Demonstrates a for loop, with _ as a variable
for _ in range(3):
    print("meow")

print("#######")

# Demonstrates str multiplication
print("meow\n" * 3, end="")

print("#######")

# Introduces continue, break
while True:
    n = int(input("What's n? "))
    if n <= 0:
        continue
    else:
        break

for _ in range(n):
    print("meow")

print("#######")

# Removes continue
while True:
    n = int(input("What's n? "))
    if n > 0:
        break

for _ in range(n):
    print("meow")

print("#######")


# Demonstrates defining functions
def main():
    meow(get_number())


def get_number():
    while True:
        n = int(input("What's n? "))
        if n > 1:
            return n


def meow(n):
    for _ in range(n):
        print("meow")


main()
