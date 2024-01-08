def get_fraction_input():
    while True:
        try:
            x, y = map(int, input("Fraction (x/y): ").split("/"))
            if y == 0 or x > y:
                raise ValueError("Invalid fraction")
            break
        except ValueError:
            print("Invalid input. Please enter a valid fraction.")

    return x, y


def calculate_percentage(x, y):
    percentage = round(x / y * 100)
    return percentage


def main():
    x, y = get_fraction_input()
    percentage = calculate_percentage(x, y)

    if percentage <= 1:
        print("E")
    elif percentage >= 99:
        print("F")
    else:
        print(f"{percentage}%")

if __name__ == "__main__":
    main()
