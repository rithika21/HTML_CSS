f1=input()
f2=input()
n=f1+" "+f2
print(n)
print(f1.upper())
print("18 - 2 - 2003".split("-"))



class Customer:

    def __init__(self, name, type):
        self.name=name
        self.type=type

        if(type == "senior"):
            self.interest= 7.5

        else:
            self.interest=6

    def get_interest_on_deposit(self,principle, years):
        interest = principle*years* self.interest
        return interest

customer1 = Customer("Nikita","normal")
customer2 = Customer("Jayanthi", "senior")
print(customer1.get_interest_on_deposit(200000,3))
print(customer2.get_interest_on_deposit(200000,3))



class Customer:

    def __init__(self, name, type):
        self.name=name
        self.type=type

        if(type == "senior"):
            self.interest= 7.5

        else:
            self.interest=6

    def get_interest_on_deposit(principle, years):
        interest = principle*years* self.interest
        return interest_amount 

customer1 = Customer("rithika","normal")
customer2 = Customer("rithi", "senior")
print(customer1.get_interest_on_deposit(200000,3))
print(customer2.get_interest_on_deposit(200000,3))
