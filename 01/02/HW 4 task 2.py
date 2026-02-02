#[1, 3, 5] => 30
#[6] => 36
#[] => 0

first_list = [6]
second_list = first_list [0::2]
a = sum(second_list)
if first_list == []:
    print(0)
else:
 b = int(first_list[-1] * a)
 print(b)
# спробував трохи інакше + додав умову для first_list наче запрацювало , пробува перший раз через цикл як на відео ви просили , тяжко не врахував про []
#  а print то для себе залишав щоб бачити як працює :)
#action_1 = 0
#for x in second_list:
    #action_1 =  action_1 + x
#resolt = action_1 * first_list [-1]
#print(action_1)
#print(resolt)