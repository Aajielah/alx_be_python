def perform_operation(num1, num2, operation):
    match operation:
        case "+":
            result = float(num1) + num2
            print(f"The result is {result}")
        case "-":
            result = num1 - num2
            print(f"The result is {result}")
        case "*":
            result = num1 * num2
            print(f"The result is {result}")
        case "/":
            if num2 == 0:
                print("Cannot divide by zero.")
            else:
                result = num1 / num2
                print(f"The result is {result}")

