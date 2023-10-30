# n = 234
# print(str(n)[1])
# #output 3
def common(a,b,c):
    for i in a:
        if i in b and i in c:
            print(i)
            break
        else:
            print(-1)
        
    

a = input()
b = input()
c = input()
