from collections import defaultdict

item_counts = defaultdict(int)

while True:
    try:
        item = input("").upper()
    except EOFError:
        print()
        break

    item_counts[item] += 1

for item, count in sorted(item_counts.items()):
    print(f"{count} {item}")
