n = int(input())


arr = input().split()
if len(arr)==0:
    print("NULL")
else:
    k = int(input())%len(arr)
    f = arr[:k]
    last = arr[k:]
    print(*(last+f), sep=" ")
    
# input
# 6
# a s d  f g h
# 3
# output

# f g h a s d
        


