number = int(input("enter your number: "))
while number > 9:
    number_str = str(number)
    result = 1
    for digit in number_str:
        result = result * int(digit)
    number = result
print('the result is: ', number)