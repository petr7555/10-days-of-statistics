from math import factorial

def bin(x,n,p):
    return (factorial(n)/(factorial(x)*factorial(n-x)))*(p**x)*((1-p)**(n-x))
    
ratio = 1.09
p = ratio/(ratio+1)
result = 0
at_least = 3
total = 6
for i in range(at_least,total+1):
    result += bin(i,total,p)

print(round(result,3))
