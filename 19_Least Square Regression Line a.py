from sklearn import linear_model

m, n = map(int, input().split())
x = []
y = []
for i in range(n):
    inp = list(map(float, input().split()))
    x.append(inp[:-1])
    y.append(inp[-1])

lm = linear_model.LinearRegression()
lm.fit(x, y)
a = lm.intercept_
b = lm.coef_

q = int(input())
for i in range(q):
    inp = list(map(float, input().split()))
    y = a + b[0] * inp[0] + b[1] * inp[1]
    print(round(y, 2))
