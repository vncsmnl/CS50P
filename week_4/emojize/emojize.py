from emoji import emojize

def main():
    try:
        user_input = input("Enter a text with emoji aliases: ")
        output = emojize(user_input, language="alias")
        print("Output:", output)
    except Exception as e:
        print("An error occurred:", e)

if __name__ == "__main__":
    main()
