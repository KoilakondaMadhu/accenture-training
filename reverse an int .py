n = 1010
val = 0
sum1 =0
while (n>0):
  rem = n%10
  res = rem*pow(2,val)
  val += 1
  sum += res
  n = n//10
print(sum)
