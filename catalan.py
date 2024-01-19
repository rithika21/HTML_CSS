def catalan(n):

    C=[]
    C.extend([1,1]) #c0 c1
    
    for i in range(2,n+1):
        temp=0
        for j in range(i):
            temp+=C[i-j-1]*C[j]
        C.append(temp)
    return C

n=20
print(catalan(n))