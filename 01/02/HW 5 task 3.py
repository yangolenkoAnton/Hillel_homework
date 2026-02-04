import string
my_string = input()
sign = string.punctuation
for item in sign:
    my_string = my_string.replace(item, "")
print("#"+ my_string.title().replace(' ', '')[:140])
#зміну sign додавав щоб бачити які символи в ході створення , то лишив вже її і залишити