n = int(input())
x = list(map(int, input().split()))
f = list(map(int, input().split()))
s = []
for i in range(n):
    for j in range(f[i]):
        s.append(x[i])
s.sort()
l = len(s)
left = s[:l//2]
right = s[l//2+l%2:]

if len(left) % 2 == 0:
    q1 = round((left[len(left)//2]+left[len(left)//2-1])/2,1)
else:  
    q1 = left[len(left)//2]

if len(right) % 2 == 0:
    q3 = round((right[len(right)//2]+right[len(right)//2-1])/2,1)
else:  
    q3 = right[len(right)//2]
    
interquartile_range = (q3 - q1)/1

print(interquartile_range)

