from math import pi, e, inf, erf

mean = 70
std_dev = 10

def find_prob(mean, std_dev, x):
    z = (x-mean)/(std_dev*(2**(1/2)))
    probability = (1/2)*(1+erf(z))
    return probability

#more than 80
prob_1 = find_prob(mean, std_dev, inf)
prob_2 = find_prob(mean, std_dev, 80)
prob_A = prob_1 - prob_2
print(round(prob_A*100,2))

#more than or equal to 60
prob_1 = find_prob(mean, std_dev, inf)
prob_2 = find_prob(mean, std_dev, 60)
prob_B = prob_1 - prob_2
print(round(prob_B*100,2))

#less than 60
prob_C = find_prob(mean, std_dev, 60)
print(round(prob_C*100,2))
