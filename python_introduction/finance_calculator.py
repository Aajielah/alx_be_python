# savings_calculator.py

# Prompt user for monthly income and expenses
monthly_income = float(input("Enter your monthly income: "))
monthly_expenses = float(input("Enter your total monthly expenses: "))

# Calculate monthly savings
monthly_savings = monthly_income - monthly_expenses

# Calculate projected annual savings with 5% interest
projected_annual_savings = monthly_savings * 12 * (1 + 0.05)

# Display results
print(f"Your monthly savings are: {monthly_savings}")
print(f"Your projected annual savings after including interest are: {projected_annual_savings}")
