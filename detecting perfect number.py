
n = int(input())
sum = 0

for i in range(1, n + 1):
    if n % i == 0:
        sum += i

if sum == 2 * n:  # Checking if the sum of divisors (excluding itself) is equal to 2 times the number
    print("Yes")
    print(1)
else:
    print("No")
    print(sum - n)  # Excluding the number itself from the sum




# n =int(input())
# sum =0 
# for i in range(1,n):
#     if n % i == 0:
#         sum += i
# if sum == n :
#     print("yes")
#     print(1)
# else:
#     print("No")
#     print(sum)