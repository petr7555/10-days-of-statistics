from math import factorial, e

mean = 2
k = 3

result = ((mean**k)*(e**(-mean)))/(factorial(k))
print(round(result,3))
