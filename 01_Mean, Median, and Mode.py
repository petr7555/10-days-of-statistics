n = int(input())
x = list(map(int,input().split()))
x.sort()

mean = round(sum(x)/n,1)

if n % 2 == 0:
    median = round((x[n//2]+x[n//2-1])/2,1)
else:  
    median = x[n//2]
    
dict = {}
for num in x:
    if num in dict:
        dict[num] += 1
    else:
        dict[num] = 1
        
max_occur = -1
modus = 0
for key in dict:
    if dict[key] > max_occur or (dict[key] == max_occur and key < modus):
        max_occur = dict[key] 
        modus = key
    
print(mean)
print(median)
print(modus)
