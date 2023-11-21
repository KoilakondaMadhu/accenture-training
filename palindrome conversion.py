def palindrome(num):
    return num == num[::-1]
n = input()
sum  = int(n) + int(n[::-1])
while not palindrome(str(sum)):
    n = str(sum)
    sum = int(n) + int(n[::-1])
print(sum)
n = int(input())
palindrome(n)