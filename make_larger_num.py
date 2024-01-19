elements = [34, 7, 91, 9, 1, 20, 10]
#EX1. What is the max number you can create by attaching/connecting elements of this array?
#ans: 9 91 7 34 20 1 10 => 99173420110
elements2=[]
for i in range(0,len(elements)):
    elements2.append(str(elements[i]))
print(elements2)
def double_num(x):
    return x*2  #replicate the given string for the index value of dictionary
elements2.sort(key=double_num,reverse=True)
print(int("".join(elements2)))

