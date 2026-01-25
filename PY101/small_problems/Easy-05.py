# P
# Prompt the user for a number (amount of their bill at a restaurant)
# Prompt the user for a tip % they want to give
# Compute the tip based on the bill amount
# Print the tip amount in $ and the total bill amount in $ (original bill $ + tip $)

# E
# bill = 24.50, tip = 20%, tip = 4.9, total bill = (24.5 + 4.9) = 29.40

# D
# input1 is string, input2 is string
# both inputs will need to be converted to float

# A
# Ask and receive input1, convert to float. Ask and receive input2, convert to float.
# Convert input 2 to a decimal (divide it by 100)
# Multiply newly calculated decimal by original bill total (input 1) and assign to a variable tip_amount
# Add this amount to the original bill and assign to variable total_bill
# Print tip_amount, print total_bill

# C

print("Hi, this is a tip calculator. Please input the following.")
og_bill = float(input("What is the total cost of your meal? "))
tip = float(input(f"How much would you like to tip? (Write 15% as 15) "))
tip_decimal = tip / 100
tip_amount = tip_decimal * og_bill
total_bill = og_bill + tip_amount

print(f"Your tip amount is ${tip_amount:.2f}.")
print(f"Your total bill is ${total_bill:.2f}.")
