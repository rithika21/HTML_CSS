#Problem statement : Upto N, i need to find all (a, b, c)triplets
#also i want to have a count of three.

N=int(input("Enter the value of N:"))

count=0
#looping
#rnage(x,y)=start from x, go upto y-1
for a in range(1,N+1):
    for b in range(a,N+1):   
        for c in range(b,N+1):
            #print (a ,b, c)
            if c*c == (a*a +b*b):
                print(a,b,c)
                count=count+1

print("\n total triplets found: ",count)