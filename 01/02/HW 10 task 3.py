def is_even(digit):
    number = digit % 2
    if number == 0:
        return True
    else:
        return False
assert is_even(2) == True, 'Test1'
assert is_even(5) == False, 'Test2'
assert is_even(0) == True, 'Test3'
print('OK')