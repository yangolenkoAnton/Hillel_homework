import string
import keyword

name = input("enter name: ")
valid = True
if name and name[0].isdigit():
    valid = False
for item in name:
    if item.isupper():
        valid = False
if " " in name:
    valid = False
for item in string.punctuation:
    if item != "_" and item in name:
        valid = False
if all( item == "_" for item in name):
    valid = False
    if len(name) == 1:
        valid = True
    else:
     valid = False
if name in keyword.kwlist:
    valid = False
print(valid)
