l = list(map(int,input().split()))
sum = 0

for i in range(len(l)):
    sum += (i+1)**2-l[i]
print(sum)
    
