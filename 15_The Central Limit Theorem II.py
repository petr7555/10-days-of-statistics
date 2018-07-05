from math import sqrt, e, erf

maximum = 250
n = 100
mean = 2.4
std_dev = 2

mean_comma = n * mean
std_dev_comma = sqrt(n) * std_dev

def find_prob(mean, std_dev, x):
    z = (x-mean)/(std_dev*(2**(1/2)))
    probability = (1/2)*(1+erf(z))
    return probability

prob = find_prob(mean_comma, std_dev_comma, maximum)    
print(round(prob, 4))
