try:
    x, y, z = input("Expression: ").split()
    x, z = float(x), float(z)

    if y not in ['+', '-', '*', '/']:
        raise ValueError("Invalid operator. Please use +, -, *, or /.")

    if y == '/' and z == 0:
        raise ValueError("Division by zero is not allowed.")

    if y == '/' and z == 0:
        raise ValueError("Division by zero is not allowed.")

    ans = eval(f"{x} {y} {z}")

    print(f"Result: {ans:.1f}")

except ValueError as ve:
    print(f"Error: {ve}")

except Exception as e:
    print(f"An unexpected error occurred: {e}")
