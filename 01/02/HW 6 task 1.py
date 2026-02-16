import string

letters1 = input("enter two letters (a-d): ")
parts = letters1.split('-')
start_letter = parts[0]
end_letter = parts[1]
start_index = string.ascii_letters.index(start_letter)
end_index = string.ascii_letters.index(end_letter)
result = string.ascii_letters[start_index:end_index + 1]
print(result)