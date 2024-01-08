from random import randint

def get_valid_input(prompt, error_message, condition):
    while True:
        try:
            value = int(input(prompt))
            if condition(value):
                return value
            else:
                print(error_message)
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

def main():
    level = get_valid_input("Enter the level: ", "Level must be greater than 0.", lambda x: x > 0)

    secret_number = randint(1, level)

    while True:
        try:
            guess = get_valid_input("Enter your guess: ", "Invalid guess. Please enter a valid integer.", lambda x: True)

            if guess < secret_number:
                print("Too small!")
            elif guess > secret_number:
                print("Too large!")
            else:
                print("Just right!")
                break
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

if __name__ == "__main__":
    main()
