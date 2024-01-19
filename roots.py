#PS1 : POINT IN OUT OR ON THE CIRCLE
# INPUT X1 Y1 R
#X2 Y2
# OUTPUT :
#INSIDE"/OUTSIDE"/"ON THE CIRCLE"
#PS2: 
#INPUT : A B C
#OUPUT : SIDES ANGLE TRIANGLE
#sides=["equi","iso","scalen"]
#angle=["right","obtuse","acute"]
#print : not a valid triangle
a1,a2,a3=list(map(int,input().split()))
if(a1==a2 and a2==a3 and a3==a1):

    print("equivateral triangle")
    print("acute angle")

elif(a1==a2 or a2==a3 or a3==a1):

    print("Isoceles triangle")

else:

    print("Scalene triangle")
