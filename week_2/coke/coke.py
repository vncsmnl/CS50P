def calculate_change_due(due, inserted):
    return inserted - due

def main():
    due, inserted = 50, 0

    while inserted < due:
        print("Amount Due:", due - inserted)

        try:
            coin = int(input("Insert Coin: "))
            if coin in [5, 10, 25]:
                inserted += coin
            else:
                print("Invalid coin. Please insert 5, 10, or 25.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    change_due = calculate_change_due(due, inserted)
    print("Change Owed:", change_due)

if __name__ == "__main__":
    main()
