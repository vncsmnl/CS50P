import inflect

def get_names():
    names = []
    while True:
        try:
            name = input("Name (or press Enter to finish): ").strip()
            if not name:
                break
            names.append(name)
        except EOFError:
            break
    return names

def main():
    p = inflect.engine()
    names = get_names()

    if names:
        joined_names = p.join(names)
        print(f"Adieu, adieu, to {joined_names}")
    else:
        print("No names provided. Goodbye!")

if __name__ == "__main__":
    main()
