from datetime import datetime

months = [
    "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December",
]

def validate_date(date_str):
    try:
        date_obj = datetime.strptime(date_str, "%B %d, %Y")
    except ValueError:
        try:
            date_obj = datetime.strptime(date_str, "%m/%d/%Y")
        except ValueError:
            return None

    return date_obj.strftime("%Y-%m-%d")

date_valid = False

while not date_valid:
    date_input = input("Date: ")
    formatted_date = validate_date(date_input)

    if formatted_date:
        print(formatted_date)
        date_valid = True
    else:
        print("Invalid date format. Please enter a valid date.")
