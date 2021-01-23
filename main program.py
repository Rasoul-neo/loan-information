# loan information details


#getting input from miserable users
principal=float(input("enter amount of your loan: "))
annual_interest_rate=float(input("enter annual interest of your loan: "))
duration=float(input("enter duration of your loan, how many years?:"))
print("")
print("This is your loan information: ")
print("loan amount: ", principal)
print("annual interest rate is: ", annual_interest_rate, "percent")
print("loan duration: ", duration, "year")

#calculating monthly payement
def ghest(principal,annual_interest_rate,duration):
    r=(annual_interest_rate/100)/12
    n=duration*12
    monthly_payement = principal*(r*((1+r)**n))/(((1+r)**n)-1)
    print ("your monthly payement is:", monthly_payement)
ghest(principal,annual_interest_rate,duration)

#calculating remaining of loan
def remaining(principal,annual_interest_rate,duration,number_of_payement):
    r=(annual_interest_rate/100)/12
    n=duration*12
    p=number_of_payement
    remaining_loan_balance = int(principal*(((1+r)**n)-((1+r)**p))/(((1+r)**n)-1))
    print ("your remaining is: " , remaining_loan_balance)
    
#final step. giving complete information about every year loan remaining   
year=1
number_of_payement=12
while year<=duration:
    print("after the" ,year,"year")
    remaining(principal,annual_interest_rate,duration,number_of_payement)
    year+=1
    number_of_payement+=12
