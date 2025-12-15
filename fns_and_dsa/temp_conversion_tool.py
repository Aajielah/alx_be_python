CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5
FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9



# --- 2. Implement Conversion Functions ---

def convert_to_celsius(fahrenheit):
    """
    Takes a Fahrenheit value and returns Celsius
    using the global conversion factor.
    """
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR


def convert_to_fahrenheit(celsius):
    """
    Takes a Celsius value and returns Fahrenheit
    using the global conversion factor.
    """
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32


# --- 3. User Interaction & Main Execution ---

def main():
   while True:
        try:
            temperature = float(input("Enter the temperature to convert: "))
            temperature_type = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().lower()

            if temperature_type not in ("f", "c"):
                print("The temperature type has to be either F OR C ")
                continue

        except ValueError:
            print("Invalid temperature. Please enter a numeric value.")
            continue
        else:
            if temperature_type == "f" :
                print(f"{temperature} fahrenheit converted to degree celsius  is {convert_to_celsius(temperature)}")
            elif temperature_type == "c":
                    print(f"{temperature} degree celsius converted to fahrenheit is {convert_to_fahrenheit(temperature)}")
            break

# This check ensures the script runs only when executed directly
if __name__ == "__main__":
    main()