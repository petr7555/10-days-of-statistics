from math import factorial

def bin(x,n,p):
    return (factorial(n)/(factorial(x)*factorial(n-x)))*(p**x)*((1-p)**(n-x))
    
p = 0.12
at_least = 2
total = 10

result = 0
at_most = 2
for i in range(0,at_most+1):
    result += bin(i,total,p)

print(round(result,3))

result2 = 0
for i in range(at_least,total+1):
    result2 += bin(i,total,p)

print(round(result2,3))


