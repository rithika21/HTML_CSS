def balanced_paranthesis(exp):
    stack=[]
    
    for char in exp:
        if char=="(":
            stack.append(char)
        else:
            if len(stack)>0:
                stack.pop()
            else:
                #stack is empty
                return False
            
    if len(stack)>0:
        return False
    return True

                
expression="((()))()"
print(balanced_paranthesis(expression))