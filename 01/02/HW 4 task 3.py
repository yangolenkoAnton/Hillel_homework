import random
# Пункт 1
#my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#new_list = []
#for num in my_list:
    #new_list.append(random.randint(my_list[0], my_list[-1]))
    #if len(new_list) > 5:
        #break
#print(new_list)
# Пункт 2
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
new_list = []
for num in my_list:
    new_list=((my_list[0], my_list[2], my_list[-2]))
    if len(new_list) > 2:
        break
print(new_list)