import math
def solve(a, b):
    p =""
    for x in range(2*a+940):
        if all(x%i!=0 for i in range(2,int(math.sqrt(x))+1)):
            p+=str(x)
    return (p[a+2:a+2+b])
