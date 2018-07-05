n = int(input())
x = list(map(int, input().split()))

mean = sum(x)/n

squared_dist_sum = 0
for num in x:
    squared_dist_sum += (num - mean)**2

std_dev = (squared_dist_sum/n)**(1/2)

print(round(std_dev,1))
