snake_case = input().strip()

camel_case = ''.join(word.capitalize() for word in snake_case.split('_'))

print(camel_case)
