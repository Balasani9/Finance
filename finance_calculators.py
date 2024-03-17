# CAPSTONE PROJECT 1 - Variables and Control Structures

# math package required for operations like pow = power
import math

print("""\nInvestment  - to calculate the amount of interest you'll earn on your investment
Bond        - to calculate the amount you'll have to pay on a home loan""")

# while loop set up to deal with invalid selection
while True:
    # convert to lower case in case user uses capitals
    calculation = input("\nEnter either 'investment' or 'bond' from the menu above to proceed: ").lower()

    # breaks from loop if valid selection made
    if calculation == "investment": 
        print ("You have selected investment")
        break

    elif calculation == "bond":
        print("You have selected bond.")
        break

    else: 
        print ("Your selection is invalid. Please try again.")

    

# investement computation
if calculation == "investment": 
    #asking user to input relevant financial information
    money_investment = float(input ("How much money are you depositing (£)?\t"))
    interest_investment = float(input ("What is the assumed interest rate per annum (exclude % symbol)?\t"))/100
    investment_term = float(input ("How many years will you be investing for?\t"))

    # while loop set up to deal with invalid selection
    while True:
        # different formulas depending if simple or compound interest is selected
        interest = input("What kind of interest? (simple or compound)\t").lower()
        if interest == "simple":
            total_amount = money_investment * (1 + interest_investment*investment_term)
      
            # Print the total amount paid - always uses 2 decimal places and this is denominated in GBP - Pounds and Pence
            print("The total amount assuming simple interest is: £", "{0:.2f}".format(total_amount))
            
            # breaks from loop if valid selection made
            break

        elif interest == "compound":
            total_amount = money_investment * math.pow((1 + interest_investment),investment_term)
       
            # Print the total amount paid - always uses 2 decimal places and this is denominated in GBP - Pounds and Pence
            print("The total amount assuming compound interest is: £", "{0:.2f}".format(total_amount))
            break

        # if neither compound nor simple are selected prints an error message and asks again in the while loop
        else:
            print ("Invalid selection. Please try again.")

# bond computation
elif calculation == "bond":
    
    # Value of house is a float, although most likely to be an integer
    home_value = float(input("What is the current value of the house (£)?  "))
    
    # annual interest rate is converted to monthly / decimal amount
    interest_bond = float(input("What is the annual interest rate (exclude % symbol)?  "))/(100 * 12)
    
    # term in month could be a float - if the loan was in days for example so would need to be converted into months
    term_months = float(input("How many months to repay the bond?   "))
    
    # formula to calculate the monthly repayment from last 3 data items collected from the user
    monthly_repayment = (interest_bond * home_value)/(1 - (1 + interest_bond)**(-term_months))
    
    # Print the monthly repayment - always uses 2 decimal places and this is denominated in GBP - Pounds and Pence
    print("Your monthly repayment will be: £", "{0:.2f}".format(monthly_repayment))

