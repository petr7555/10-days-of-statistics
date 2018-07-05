def geom(n,p):
    return (1-p)**(n-1)*p

p = 1/3
n = 5
result = 0
for i in range(1,n+1):
    result += geom(i,p)
    
print(round(result,3))
