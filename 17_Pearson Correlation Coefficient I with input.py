n = int(input())
X = list(map(float, input().split()))
Y = list(map(float, input().split()))
mean_x = sum(X)/n
mean_y = sum(Y)/n

sum = 0
for num in X:
    sum += (num - mean_x)**2
std_dev_x = (sum/n)**(1/2)

sum = 0
for num in Y:
    sum += (num - mean_y)**2
std_dev_y = (sum/n)**(1/2)

sum = 0
for i in range(n):
    sum += (X[i]-mean_x)*(Y[i]-mean_y)
pcc = sum/(n*std_dev_x*std_dev_y)

print(round(pcc,3))
