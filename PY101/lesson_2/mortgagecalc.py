def prompt(message):
    return input(f'{message}\n>>> ')

def calc_monthly_payment(loan_amount, monthly_apr, dur_months):
    if monthly_apr == 0:
        return round(loan_amount / dur_months, 2)

    monthly_payment = (loan_amount *
        (monthly_apr / (1 - (1 + monthly_apr) ** (-dur_months))))
    return round(monthly_payment, 2)


while True:
    print("Welcome to the Mortgage Payment Calculator!")
    while True:
        loan_amount = prompt('What is your loan amount?')
        try:
            loan_amount = float(loan_amount.replace(',', '').replace(' ', ''))
            if loan_amount <= 0:
                print("Loan amount must be greater than zero.")
                continue
            break
        except ValueError:
            print("Invalid input. Please try again.")
    while True:
        apr = prompt('What is your APR? (Use 5 for 5%, rather than 0.05)')
        try:
            apr = float(apr.replace('%', '').strip())
            if apr < 0:
                print("APR cannot be less than zero.")
                continue
            monthly_apr = (apr / 100) / 12
            break
        except ValueError:
            print("Invalid input. Please try again.")
    while True:
        duration = prompt('What is the length of your loan in years?')
        try:
            duration = float(duration)
            if duration <= 0:
                print("Loan must have a defined length. Please try again.")
                continue
            dur_months = round(duration * 12)
            if dur_months <= 0:
                print("Loan duration must be at least one month.")
                continue
            break
        except ValueError:
            print("Invalid input. Please try again.")
    monthly_payment = calc_monthly_payment(loan_amount, monthly_apr, dur_months)
    print(f'''Loan Details:
    - Loan Amount: ${loan_amount}
    - APR: {apr}%
    - Duration: {dur_months} months
    Your monthly loan amount will be be ${monthly_payment}.''')
    while True:
        ans = prompt('Would you like to calculate another monthly payment?')
        ans = ans.lower().strip()
        if ans.startswith(('y', 'n')):
            break
        print("Please enter either 'y' or 'n'.")
    if ans.startswith('n'):
        print('Thank you for using the Mortgage Payment Calculator!')
        break