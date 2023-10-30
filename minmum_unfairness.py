def mins(l,k):
    l.sort()
    m = float("inf")#infinite value
    for i in range(n):
        diff = l[i+k-1]
        if diff<m:
            m = diff
    return m
   
n = int(input())
l = list(map(int,input().split()))#int list input
k = int(input())
print(mins(l,k))
       
       
       
       