from math import pi, e
from scipy import integrate

mean = 20
std_dev = 2
less_than = 19.5
upper = 22
lower = 20

def integrand(x):
    return e**(-(x**2))

def find_prob(mean, std_dev, x):
    z = (x-mean)/(std_dev*(2**(1/2)))
    i = integrate.quad(integrand,0,z)
    erf = (2/(pi**(1/2)))*i[0]
    probability = (1/2)*(1+erf)
    return probability

#less than 19.5
prob_A = find_prob(mean, std_dev, less_than)
print(round(prob_A,3))

#less than 22
prob_1 = find_prob(mean, std_dev, upper)
#less than 20
prob_2 = find_prob(mean, std_dev, lower)

prob_B = prob_1 - prob_2
print(round(prob_B,3))
