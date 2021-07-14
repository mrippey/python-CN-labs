# Take in the following three values from the user:
# 1. investment amount
# 2. interest rate in percentage
# 3. number of years to invest
#
# Calculate the future values and print them to the console.

# Formula: future value = present value x[1 + interest rate x time)]

def investment_outlook():
    amount = int(input('Enter your desired investment amount (no commas): '))
    int_rate = float(input('Enter your banking institutions interest rate percentage: '))
    num_years = int(input('Enter the number of years you would like to invest: '))

    future_value = amount * (1 + int_rate * num_years)

    return f'Future value of your investment: ${future_value:.2f}'

print(investment_outlook())