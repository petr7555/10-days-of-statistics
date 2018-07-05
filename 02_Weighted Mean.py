n = input()
x = list(map(int, input().split()))
w = list(map(int, input().split()))
s = 0
for i in range(len(x)):
    s += x[i]*w[i]
    
weighted_mean = round(s/sum(w),1)

print(weighted_mean)
