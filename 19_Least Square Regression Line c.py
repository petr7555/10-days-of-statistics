import numpy as np

m, n = map(int, input().split())
x = []
y = []
for i in range(n):
    inp = list(map(float, input().split()))
    x.append([1])
    x[i].extend(inp[:-1])
    y.append([inp[-1]])
    
x_new = []    
q = int(input())
for i in range(q):
    inp = list(map(float, input().split()))
    x_new.append([1])
    x_new[i].extend(inp)

x = np.array(x)
y = np.array(y)
x_new = np.array(x_new)

trans_x = x.transpose()
inv = np.linalg.inv(np.dot(trans_x,x))
next_step = np.dot(inv,trans_x)
result_matrix = np.dot(next_step,y)

y_new = np.dot(x_new,result_matrix)
for i in y_new:
    print(round(i[0],2))
