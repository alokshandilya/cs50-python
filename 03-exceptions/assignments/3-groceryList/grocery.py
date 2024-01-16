def main():
    grocery_dict = {}
    while True:
        count = 0
        try:
            item = input("").casefold().strip()
            if not item:
                raise KeyError
        except (KeyboardInterrupt, EOFError):
            print("\n")  # default end="\n" too (1 line space)
            break
        except KeyError:
            continue
        else:
            if item in grocery_dict:
                count = grocery_dict.get(item, 0) + 1
            else:
                count = 1
        grocery_dict[item] = count

    # sorted() returns list of tuples for dict
    grocery_dict = dict(sorted(grocery_dict.items()))
    for _ in grocery_dict:
        print(f"{grocery_dict.get(_)}", _.upper())


main()
