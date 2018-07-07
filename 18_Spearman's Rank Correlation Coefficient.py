n = int(input())
X = list(map(float, input().split()))
Y = list(map(float, input().split()))
X_s = sorted(X,reverse=True)
Y_s = sorted(Y,reverse=True)
sum = 0
for i in range(n):
    rank_x = X_s.index(X[i])
    rank_y = Y_s.index(Y[i])
    sum += (rank_x - rank_y)**2
srcc = 1-(6*sum)/(n*(n**2-1))
print(round(srcc,3))
