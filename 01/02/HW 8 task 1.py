def add_one(digits):
    number = 0
    for items in digits:
        number = number * 10 + items
    number = number + 1
    result = []
    for items in str(number):
        result.append(int(items))
    return result


assert add_one([1, 2, 3, 4]) == [1, 2, 3, 5], 'Test1'
assert add_one([9, 9, 9]) == [1, 0, 0, 0], 'Test2'
assert add_one([0]) == [1], 'Test3'
assert add_one([9]) == [1, 0], 'Test4'
print("ОК")