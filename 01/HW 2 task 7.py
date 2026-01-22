
number = int(input("Enter your number (four digits only): "))
if number <= 1000 or number>9999:
    print("wrong number")
else:
 print(number//1000)
 print((number%1000)//100)
 print((number//10)%10)
 print(number%10)
# методом підбору якщо чесно вийшло зробити, 3тє число підсказав сам python в рекомендаціїї що ввести , а з другим підібрав граючись числами сотнями і тисячами