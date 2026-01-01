def safe_divide( numerator: float, denominator: float ):
    try:
        numerator = float(numerator)
        denominator = float(denominator)
        division = numerator / denominator
    except ZeroDivisionError:
        print(f"Error: Cannot divide by zero.")
        return None
    except ValueError:
        print(f"Error: Please enter numeric values only.")
    else:
        print(f"The result of the division is {division:.2f}")
        return division


calculate = safe_divide("98" , 88)

print(calculate)