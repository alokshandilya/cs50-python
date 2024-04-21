from datetime import date
import sys
import inflect


def main():
    date = input("Enter your date of birth (YYYY-MM-DD): ")
    try:
        year, month, day = date.split("-")
    except ValueError:
        sys.exit("Invalid date of birth")
    year = int(year)
    month = int(month)
    day = int(day)
    age = age_in_words(calculate_age(year, month, day))
    print(f"{age}")


def calculate_age(year, month, day):
    current_date = date.today()
    birth_date = date(year, month, day)
    age = current_date - birth_date
    age_in_minutes = age.total_seconds() / 60
    return int(age_in_minutes)


def age_in_words(age):
    p = inflect.engine()
    words = p.number_to_words(age)
    return f"{words.capitalize().replace('and ', '')} minutes"


if __name__ == "__main__":
    main()
