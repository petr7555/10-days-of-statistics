n = int(input())
x = list(map(int, input().split()))
x.sort()
left = x[:n//2]
right = x[n//2+n%2:]

if len(left) % 2 == 0:
    q1 = round((left[len(left)//2]+left[len(left)//2-1])/2)
else:  
    q1 = left[len(left)//2]

if n % 2 == 0:
    q2 = round((x[n//2]+x[n//2-1])/2)
else:  
    q2 = x[n//2]
    
if len(right) % 2 == 0:
    q3 = round((right[len(right)//2]+right[len(right)//2-1])/2)
else:  
    q3 = right[len(right)//2]

print(q1)
print(q2)
print(q3)
