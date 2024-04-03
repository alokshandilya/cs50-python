import emoji


def print_emoji():
    emoji_input = input("Input : ")
    print(emoji.emojize(emoji_input, language="alias"))


if __name__ == "__main__":
    print_emoji()
