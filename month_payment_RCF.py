#!/usr/bin/env python3

from decimal import Decimal
import locale as lc

#function that accepts the three pieces of user input as
#arguments and then uses them to calculate the monthly payment.
def get_monthly_payment(loan_amount, yearly_rate, years):
    #Get the monthly interest rate
    monthly_interest_rate = yearly_rate/12/100
    months = years * 12
    #format the monthly payment as a decimal before calculation
    monthly_payment = Decimal("0.00")
    for i in range (months):
        monthly_payment = loan_amount*monthly_interest_rate/(
                        1-1/(1+monthly_interest_rate)**months)
    monthly_payment = monthly_payment.quantize(Decimal("1.00"))
    return monthly_payment
    
def main():
    choice = "y"
    while choice.lower() == "y":
        print("Monthly Payment Calculator\n\nDATA ENTRY")
        #get the input. assume that it is valid
        loan_amount = Decimal(input("Loan Amount:          "))
        yearly_rate = Decimal(input("Yearly Interest Rate: "))
        years = int(input("Years:                "))
        #call the monthly_payment function to calculate the amount
        monthly_payment = get_monthly_payment(loan_amount, yearly_rate, years)


        #format for localization and display the results
        result = lc.setlocale(lc.LC_ALL, "")
        if result == "C":
            lc.setlocale(lc.LC_ALL, "en_US")
        #right justify the results
        line = "{:21} {:>12}"
        
        print("\nRESULTS")
        print(line.format("Loan Amount:",
                          lc.currency(loan_amount, grouping=True)))
        print(line.format("Yearly Interest Rate:", "{:%}".format(yearly_rate/100)))
        print(line.format("Number of Years:", years))
        print(line.format("Monthly Payment:",
                          lc.currency(monthly_payment, grouping=True)))
        choice = input("\nContinue? (y/n) \n")
        
if __name__ == "__main__":
    main()
    
