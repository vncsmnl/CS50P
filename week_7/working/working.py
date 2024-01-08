import re

def main():
    print(convert(input("Hours: ")))

def convert_time_to_24_hour_format(hour, minute, period):
    if period == "PM" and hour != 12:
        hour += 12
    elif period == "AM" and hour == 12:
        hour = 0
    return hour, minute

def validate_input(start_hour, start_minute, end_hour, end_minute):
    if not (0 <= start_hour <= 23) or not (0 <= start_minute <= 59) or not (0 <= end_hour <= 23) or not (0 <= end_minute <= 59):
        raise ValueError("Invalid arguments")

def convert(s):
    if match := re.match(r"(\d{1,2}):?(\d{2})? (AM|PM) to (\d{1,2}):?(\d{2})? (AM|PM)", s):
        start_hour, start_minute, start_period, end_hour, end_minute, end_period = match.groups()

        start_hour, start_minute = convert_time_to_24_hour_format(int(start_hour), int(start_minute or 0), start_period)
        end_hour, end_minute = convert_time_to_24_hour_format(int(end_hour), int(end_minute or 0), end_period)

        validate_input(start_hour, start_minute, end_hour, end_minute)

        return f"{start_hour:02d}:{start_minute:02d} to {end_hour:02d}:{end_minute:02d}"

    raise ValueError("Invalid arguments")

if __name__ == "__main__":
    main()
