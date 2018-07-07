import numpy as np

m, n = map(int, input().split())
x = []
y = []
for i in range(n):
    inp = list(map(float, input().split()))
    x.append([1])
    x[i].extend(inp[:-1])
    y.append([inp[-1]])
    
x = np.array(x)
y = np.array(y)

trans_x = x.transpose()
inv = np.linalg.inv(np.dot(trans_x,x))
next_step = np.dot(inv,trans_x)
result_matrix = np.dot(next_step,y)

a = result_matrix[0][0]
b1 = result_matrix[1][0]
b2 = result_matrix[2][0]

q = int(input())
for i in range(q):
    inp = list(map(float, input().split()))
    y = a + b1 * inp[0] + b2 * inp[1]
    print(round(y, 2))
