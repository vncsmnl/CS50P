from datetime import date
import inflect
import sys


def calculate_total_minutes(birth_date, today):
    return (today - birth_date).days * 24 * 60


def get_birth_date():
    try:
        return date.fromisoformat(input("Date of Birth: "))
    except ValueError:
        sys.exit("Invalid input.")


def main():
    birth_date = get_birth_date()
    total_minutes = calculate_total_minutes(birth_date, date.today())

    p = inflect.engine()
    minutes_word = p.plural('minute', total_minutes)

    print(f"{p.number_to_words(total_minutes, andword='').capitalize()} {minutes_word}")


if __name__ == "__main__":
    main()
