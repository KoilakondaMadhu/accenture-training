num = int(input("Enter an integer: "))  # Input the integer
reversed_num = 0

while num > 0:
    # Get the last digit of the number
    last_digit = num % 10
    # Append the last digit to the reversed number
    reversed_num = reversed_num * 10 + last_digit
    # Remove the last digit from the original number
    num = num // 10

print("Reversed integer:", reversed_num)
