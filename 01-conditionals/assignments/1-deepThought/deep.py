x = input("Answer of Great Question of Life, the Universe, and Everything? ")
x = x.casefold().strip()
# https://docs.python.org/3/library/stdtypes.html#str.casefold
# https://docs.python.org/3/library/stdtypes.html#str.strip

if x == "42":
    print("Yes")
elif x == "forty two" or x == "forty-two":
    print("Yes")
else:
    print("No")
