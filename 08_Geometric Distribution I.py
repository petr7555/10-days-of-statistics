def geom(n,p):
    return (1-p)**(n-1)*p

p = 1/3
n = 5

print(round(geom(n,p),3))
