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
        return None
    else:
        division = round(division, 1)
        print(f"The result of the division is {division:.1f}")
        return division
