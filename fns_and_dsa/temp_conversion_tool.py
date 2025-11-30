# temp_conversion_tool.py

# --- 1. Define Global Conversion Factors ---
# These are global variables. They are accessible inside any function below.
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9



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
   temprature = float(input("Enter the temperature to convert: "))
   type = input("Is this temperature in Celsius or Fahrenheit? (C/F): ")

   if type == "F" or "f":
       print(f"{temprature} fahrenheit converted to degree celsius  is {convert_to_celsius(temprature)}")

   elif type == "C" or "c":
       print(f"{temprature} degree celsius converted to fahrenheit is {convert_to_fahrenheit(temprature)}")

# This check ensures the script runs only when executed directly
if __name__ == "__main__":
    main()