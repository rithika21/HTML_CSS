#PS:distance between 2 points
#X1 Y1
#X2 Y2

#a1=int(input("enter the number a1 : "))
#b1=int(input("enter the number b1 : "))
#a2=int(input("enter the number a2 : "))
#b2=int(input("enter the number b2 : "))
a1,a2=list(map(int,input().split()))
b1,b2=list(map(int,input().split()))
distance=(((a1-a2)*(a1-a2))+((b1-b2)*(b1-b2)))**(0.5)
print(distance)

#OUTPUT
#DISTANCE  BETWEEN THESE TWO POINTS
#hint a,b=list(map(int,input().split()))