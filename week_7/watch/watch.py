import re

def main():
    html_input = input("HTML: ")
    result = parse(html_input)
    print(result)

def parse(s):
    pattern = r'<iframe.*?src="(https?://(?:www\.)?youtube\.com(?:/embed)?/[a-zA-Z0-9_-]+)".*?'
    match = re.match(pattern, s)

    if match:
        url = match.group(1).split("/")[-1]
        return f"https://youtu.be/{url}"

    return None

if __name__ == "__main__":
    main()
