#[1, 3, 5] => 30
#[6] => 36
#[] => 0

first_list = [1, 3, 5]
second_list = first_list [0::2]
print(second_list)
action_1 = 0
for x in second_list:
    action_1 =  action_1 + x
resolt = action_1 * first_list [-1]
print(action_1)
print(resolt)