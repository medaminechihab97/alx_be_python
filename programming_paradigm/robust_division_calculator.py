def safe_divide(numerator, denominator):
    try:
        numerator = input("Enter the numerator: ")
        denominator = input("Enter the denominator: ")
        float(numerator)
        float(denominator)
        division = numerator / denominator
    except ZeroDivisionError:
        print("Error: Can not divide by zero.")

