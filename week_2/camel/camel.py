camel_case = input("camelCase: ").strip()

snake_case = ''.join(['_' + char.lower() if char.isupper() else char for char in camel_case])
print("snake_case:", snake_case)
