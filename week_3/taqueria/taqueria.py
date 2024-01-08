def calculate_total(menu, order):
    total = 0
    for item in order:
        if item in menu:
            total += menu[item]
    return total

def main():
    menu = {
        "Baja Taco": 4.00,
        "Burrito": 7.50,
        "Bowl": 8.50,
        "Nachos": 11.00,
        "Quesadilla": 8.50,
        "Super Burrito": 8.50,
        "Super Quesadilla": 9.50,
        "Taco": 3.00,
        "Tortilla Salad": 8.00,
    }

    order = []
    while True:
        try:
            item = input("Item: ").title()
            if item == "Done":
                break
            elif item in menu:
                order.append(item)
                print(f"Added {item} to the order. Current total: ${calculate_total(menu, order):.2f}")
            else:
                print("Invalid item. Please choose from the menu.")
        except EOFError:
            print()
            break

    print(f"Final Order: {', '.join(order)}")
    print(f"Total: ${calculate_total(menu, order):.2f}")

if __name__ == "__main__":
    main()
