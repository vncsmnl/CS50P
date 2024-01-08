try:
    user_input = input("Enter a sentence: ")
    words = user_input.split()
    result = "...".join(words)
    print("Joined with ellipses:", result)
except Exception as e:
    print("An error occurred:", str(e))
