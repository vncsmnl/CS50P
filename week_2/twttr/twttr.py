# Get input from the user
s = input("Input: ")

# Use a set for faster vowel checking
vowels = set("aeiou")

# Remove vowels from the input string
ans = "".join([ch for ch in s if ch.lower() not in vowels])

# Print the output
print("Output:", ans)
