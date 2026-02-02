while True:
     number_1 = int(input("Enter first number: "))
     number_2 = int(input("Enter second number: "))
     operation = (input("Enter operation (+, -, *, /): "))
     if operation == "+" or operation =="-" or operation == "*" or operation == "/":
      print("your answer is: ", end="")
     else:
        print("wrong operation")
     if operation == "+":
      print(number_1 + number_2)
     elif operation == "-":
      print(number_1 - number_2)
     elif operation == "*":
      print(number_1 * number_2)
     elif operation == "/":
      if number_2 == 0:
        print("you cannot divide by 0")
      else:
         print(number_1 / number_2)
     print("do you whant to continue? (y/n): ")
     y = input("")
     while y == "y" or y == "Y":
         number_1 = int(input("Enter first number: "))
         number_2 = int(input("Enter second number: "))
         operation = (input("Enter operation (+, -, *, /): "))
         if operation == "+" or operation == "-" or operation == "*" or operation == "/":
             print("your answer is: ", end="")
         else:
             print("wrong operation")
         if operation == "+":
             print(number_1 + number_2)
         elif operation == "-":
             print(number_1 - number_2)
         elif operation == "*":
             print(number_1 * number_2)
         elif operation == "/":
             if number_2 == 0:
                 print("you cannot divide by 0")
             else:
                 print(number_1 / number_2)
         print("do you whant to continue? (y/n): ")
         y = input("")
     if y == "n" or y == "N":
         break









