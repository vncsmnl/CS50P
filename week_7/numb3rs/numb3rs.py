import re

def main():
    ip_address = input("IPv4 Address: ")
    print(validate(ip_address))

def validate(ip):
    ip_pattern = re.compile(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$")
    if not ip_pattern.match(ip):
        return False

    octets = [int(num) for num in ip.split(".")]
    if any(num < 0 or num > 255 for num in octets):
        return False

    return True

if __name__ == "__main__":
    main()
