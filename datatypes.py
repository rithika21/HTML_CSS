# 1.NUMBERS: int, float, bool
# PS : Calculate factorials, N!= 1*2*3*4....*N
N=int(input("Enter the number:"))

factorial = 1
for i in range(1, N+1):
    factorial = factorial*i
print(factorial) 


# PS: Take inputs (a,b,c) and tell the roots of ax^2 + bx +c =0

a=int(input("Enter the first number:"))
b=int(input("Enter the second number:"))
c=int(input("Enter the third number:"))

root1=((-b) + (((b*b) - (4*a*c))**0.5))/(2*a)
root2=((-b) - (((b*b) - (4*a*c))**0.5))/(2*a)

print("roots:",root1,root2)



# 2.STRINGS

a='RITHIKA'
print(a)

#Slicing: string[start:end:jump]

print(a[2])
print(a[:3])
print(a[::2])
print(a[::-1])

#PS : Check if input is the palindrome or not
string = input("Check palindrome for: ")
print(string == string[::-1])

#Operation with strings
fname= "RITHIKA"
lname= "VENKATAHALAM"

fullname = fname + " "+ lname  # '+' with strings, mean concatenation
print(fullname)

print(fname*3)  # '+' of strings means repeat it that many times.

# 3.LISTS
squares_1=[1,4,9,16,25]
squares_2=[36,49,64,81,100]
 #Intended squares = [1,.....100]
squares = squares_1 + squares_2  #Adding two lists, concatenate them

squares.append(121)  #append adds element to the last
print(squares)

squares.pop()   #pop removes last element
print(squares)

#slicing works on lists
print(squares[1::2])

print(squares[::-1])

print(squares, len(squares))


#PS: what is the max number you can create by attaching/ connecting elements of this array
#9 91 7 34 20 1 10 => 99173420110
elements=[34,7,91,9,1,20,10]
elements2=["34","7","91","9","1","20","10","3","32"]

def double_num(x):
    return x*2

elements2.sort(key=double_num,reverse=True)

print(int("".join(elements2)))
# 4.TUPLES

# 5.SETS

#PS: Tell me how many unique names are there in the list?
names = ["rithi","latha","veenkat","rithi","laks","vans","kavya","niva"]
print(set(names), len(set(names)))

#PS: Tell me how many unique characters are there
name="rithi"
print(set(name), len(set(name)))

set1={1,2,3,2,3}
set2={3,4,5,3}
print(set1)
print(set2)

#set operation
print(set1 | set2)     #Union
print(set1 & set2)     #Intersection
print(set1 - set2)     #Left Difference
print(set2 - set1)     #Right Difference

# 6.DICTIONARIES

#Till now, in lists/arrays, you you have done indexing like this.

array = [9.81,3.14,1.73,1.61,2.71]
# [gravity constant, pi, root_3, golden_ratio, euler_number]
print(array[1])

#Can I do this? array["pi"]

capitals={
    "India":"Delhi",
    "Germany":"Berlin",
    "USA":"Washington DC",
    "Australia":"Canberra"
    #"key" : "value" pair
}

print(capitals["Germany"])

constants={
    "pi":3.14,
    "golden_ratio": 1.61,
    "gravity": 9.81
}
print(constants["gravity"])

exam_marks = {
    "rithika":{
        "physics" : 60,
        "chemistry" : 95,
        "maths" : 99
    }
}
print(exam_marks["rithika"]["maths"])

print(exam_marks.keys())
print(exam_marks.values())
print(exam_marks.items())
print(len(exam_marks))

#########################################################################################################################
# sequence and non-sequence data types:
#string-sequence of characters
#non - sequence data types=1
#sequence data types = 5


