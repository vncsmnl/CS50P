import sys
import requests

def get_current_price():
    try:
        response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
        response.raise_for_status()  # Raise an exception for bad HTTP responses
        data = response.json()
        return data["bpi"]["USD"]["rate_float"]
    except requests.RequestException as e:
        print(f"Error fetching current price: {e}")
        sys.exit(1)

def main():
    if len(sys.argv) != 2:
        sys.exit("Usage: python script.py <amount>")

    try:
        amount = float(sys.argv[1])
    except ValueError:
        sys.exit("Error: The provided amount is not a valid number")

    current_price = get_current_price()
    result = amount * current_price
    print(f"${result:,.4f}")

if __name__ == "__main__":
    main()
