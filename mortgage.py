#Get user input for mortgage loan pricipal,percent annual interest and years to pay off mortgage

mortgage_loan_principal=int(input("Enter Mortgage loan: "))
interest=float(input("Enter interest: "))
percent_interest=interest/100
Years_to_pay_off_mortgage=int(input("Enter years to pay off mortgage: "))

#Calculate monthly payement,amount to pay in months for mortgage,interest rate for monthly percentage,Total amount

Amount_in_months_to_pay_mortgage=Years_to_pay_off_mortgage*12
Interest_rate_monthly_percent=percent_interest/12
monthly_payment=mortgage_loan_principal*(Interest_rate_monthly_percent*((1+Interest_rate_monthly_percent)**Amount_in_months_to_pay_mortgage))/(((1+Interest_rate_monthly_percent)**Amount_in_months_to_pay_mortgage)-1)
print(f"For a {Years_to_pay_off_mortgage}-year mortgage loan of ${mortgage_loan_principal} at annual interest rate of {interest}% you pay ${monthly_payment:.2f} monthly") 
Total_amount=monthly_payment*Amount_in_months_to_pay_mortgage
print(f"Total amount paid will be ${Total_amount:.2f}")