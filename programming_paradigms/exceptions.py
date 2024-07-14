def division(x , y):
    if y == 0:
        raise ZeroDivisionError("you can not devide by zero!")
    print( x / y)

x = int(input("Enter the number you want to devide: "))
y = int(input("Enter the number you want to devide by: "))
division(x , y)
