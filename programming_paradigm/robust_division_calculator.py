def safe_divide(numerator, denominator):
    try:
        numerator = float(input("Enter the numerator: "))
        denominator = float(input("Enter the denominator: "))
        division = numerator / denominator
    except ZeroDivisionError:
        print("you can not divide by zero!")

