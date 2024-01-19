#ps : count all the primes from m to n . primt those primes as well 

M=int(input("enter starting number :"))
N=int(input("enter ending number :"))
count=0
#jump to here
def is_prime(x):
    for a in range(2,x):
        if x%a==0:
            #not a prime
            return False
    #this is prime
    return True
for i in range(M,N+1):
    #print(i) 
    if is_prime(i):# function call : jump from here6
        
        count=count+1
        print(i)
        
print("\ntotal prime numbers: ",count)