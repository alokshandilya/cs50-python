import random


def main():
    level = get_level()
    score = 0

    for i in range(10):
        x, y = generate_integer(level)
        correct_answer = x + y
        for _ in range(3):
            try:
                guess_answer = int(input(f"{x} + {y} = "))
            except ValueError:
                print("EEE")
                if _ == 2:
                    print(f"{x} + {y} = {correct_answer}")
                continue
            else:
                if correct_answer == guess_answer:
                    score += 1
                    break
                else:
                    print("EEE")
                    if _ == 2:
                        print(f"{x} + {y} = {correct_answer}")
    print("Score:", score)


def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level in [1, 2, 3]:
                return level
        except ValueError:
            continue


def generate_integer(level):
    if level == 1:
        x = random.randint(0, 9)
        y = random.randint(0, 9)
    elif level == 2:
        x = random.randint(10, 99)
        y = random.randint(10, 99)
    elif level == 3:
        x = random.randint(100, 999)
        y = random.randint(100, 999)
    return x, y


if __name__ == "__main__":
    main()
