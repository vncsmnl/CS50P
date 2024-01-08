try:
    user_input = input("Enter a text with emoticons: ")
    replaced_text = user_input.replace(":)", "🙂").replace(":(", "🙁")
    print("Replaced text:", replaced_text)
except Exception as e:
    print("An error occurred:", str(e))
