import inflect

p = inflect.engine()


def enter_names():
    names_list = []

    while True:
        try:
            names_list.append(input("Name: "))
        except EOFError:
            break

    names = p.join(names_list)
    print("Adieu, adieu, to", names)


if __name__ == "__main__":
    enter_names()
