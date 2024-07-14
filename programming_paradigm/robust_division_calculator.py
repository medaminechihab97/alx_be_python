def safe_divide(numerator, denominator):
    try:
        float(numerator)
        float(denominator)
        division = numerator / denominator
        print(f"The result of the division is {division}")
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")
    except ValueError:
        print("Error: Please enter numeric values only.")


