def safe_divide(numerator, denominator):
    try:
        float(input("Enter the numerator: "))
        float(input("Enter the denominator: "))
        division = numerator / denominator
    except ZeroDivisionError:
        print("you can not divide by zero!")
            
