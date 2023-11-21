row = int(input("Enter the number of rows: "))
col = int(input("Enter the number of columns: "))
arr = []

print("Enter the elements for each row:")

for i in range(row):
    temp = list(map(int, input().split()))
    temp.sort()
    print(*temp,sep = " ")

# 3
# 4
# 5 2 8 1
# 9 4 7 3
# 6 5 2 0
