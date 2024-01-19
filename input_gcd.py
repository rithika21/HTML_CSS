a, b=list(map(int,input().split()))

def gcd(a, b):
    #base condition
    if a%b== 0:
        return b
    #decomposition
    ans= gcd(b,a%b)
    #recognition
    return ans

print(gcd(a,b))

