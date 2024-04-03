import random

while True:
    try:
        level = int(input("Level: "))
        random_level = random.randint(0, level)
        while True:
            try:
                guess = int(input("Guess: "))
            except ValueError:
                continue
            if guess < random_level:
                print("Too small!")
            elif guess > random_level:
                print("Too large!")
            else:
                print("Just right!")
                raise EOFError
    except ValueError:
        continue
    except EOFError:
        break
