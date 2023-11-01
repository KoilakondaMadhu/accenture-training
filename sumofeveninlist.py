# write the fuction to calculate the sum of the even numbers in the given list of integers.
# the funtion shounld take a list of integers as input and return the sum of all even numbers
# in the list
# ip = 1 2 3 4 5 6 
# op = 12(2+4+6)
from typing import List

def sum_even(a: List[int]) -> int:
    b = 0  # Initialize a variable to store the sum of even numbers
    for i in a:
        if i % 2 == 0:  # Check if the number is even
            b += i  # Add the even number to the sum
    return b  # Return the sum of even numbers

# Example usage:
input_list = [1, 2, 3, 4, 5, 6]
result = sum_even(input_list)
print(result)  # This will print 12, which is the sum of even numbers (2 + 4 + 6) in the list.



l = list(map(int, input().split()))
sum = 0

for i in l:
    if i % 2 == 0:
        sum += i

print(sum)
