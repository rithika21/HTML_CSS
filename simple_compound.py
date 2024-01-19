principal = float(input("enter pa: "))
rate_of_interest=float(input("enter rate_of_interest: "))
num_of_years=float(input("enter no of years: "))

choice=int(input("\nwhat interest you want?\n1.Simple interest\n2.Compound interest\n"))

#Branching
if choice == 1:
    #calculate simple interest
    simple_interest_amount=(principal*rate_of_interest*num_of_years)/100
    print("Simple Interest",simple_interest_amount)
elif choice==2:
    #calculate compound interest
    compound_interest_amount=principal*(1+rate_of_interest/100)**num_of_years-principal
    print("Compound Interest",compound_interest_amount)
else:
    print("invalid choice\n")
