s = list(input())
res = ""
for i in s:
    if s.count(i)%2 != 0 and i not in res:
        res += i
if len(res) == 0:
    print("Empty String")
else:
    print(res)