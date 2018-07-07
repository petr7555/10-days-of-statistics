from math import sqrt, e, erf

n = 100
mean_comma = 500
std_dev_comma = 80
z = 1.96
mean = mean_comma
std_dev = std_dev_comma / sqrt(n) 
A = mean - z * std_dev
B = mean + z * std_dev

def find_prob(mean, std_dev, x):
    z = (x-mean)/(std_dev*(2**(1/2)))
    probability = (1/2)*(1+erf(z))
    return probability

prob1 = find_prob(mean, std_dev, A)
prob2 = find_prob(mean, std_dev, B)
print(round(A, 2))
print(round(B, 2))
print(round(prob1, 2))
print(round(prob2, 2))
print(round(prob2-prob1, 2))
