n = 1729
sum1 = 0
s = str(n)

for i in s:
    sum1 += int(i)

sum1 = str(sum1)
rev = sum1[::-1]
res = int(sum1) * int(rev)

if res == n:
    print('Magical Number')
else:
    print('Not a Magical Number')



# n  = 1729
# s1     sum of digits //2+7+9+1    => 19
# s2     reverse the sum            =>91
# s3     step1 * step2    91*19     =>1729


