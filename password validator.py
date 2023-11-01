# Question 9: Password Validator

# You are given a string str. Your task is to find the number of checks that are not satisfied by the string str by checking the validation of the string str if it's a strong password or not. A

# password is a strong password only if:

# ⚫ It contains at least 6 characters and at most 22 characters.

# It must contain at least one uppercase character.

# ⚫ It must contain at least one lowercase character.

# It must contain at least one special character (@, !, &, ^, %, *. #).

# It must contain at least one numeric value.

# It must not contain any two same consecutive characters.

# Input Format:

# ⚫ The input consists of a single line:

# The first line contains a string str.

# Output Format:

# 0 Print the number that represents the number of checks it is not satisfied by the str.

# Constraints



s = input()
check = 0

if not (6 <= len(s) <= 22):
    check += 1

up = 0
lo = 0
d = 0
sp = 0

for i in range(len(s)):
    if s[i].isupper():
        up += 1
    elif s[i].islower():
        lo += 1
    elif s[i].isdigit():
        d += 1
    else:
        sp += 1

if up < 1:
    check += 1
if lo < 1:
    check += 1
if d < 1:
    check += 1
if sp < 1:
    check += 1

for i in range(len(s) - 1):
    if s[i] == s[i + 1]:
        check += 1
        break

print(check)












# def is_valid_password(s):
#     checks_not_satisfied = 0

#     # Check if the length is within the required range.
#     if not (6 <= len(s) <= 22):
#         checks_not_satisfied += 1

#     # Check for at least one uppercase character.
#     if not any(char.isupper() for char in s):
#         checks_not_satisfied += 1

#     # Check for at least one lowercase character.
#     if not any(char.islower() for char in s):
#         checks_not_satisfied += 1

#     # Check for at least one special character.
#     special_characters = set('@!&^%*#')
#     if not any(char in special_characters for char in s):
#         checks_not_satisfied += 1

#     # Check for at least one numeric value.
#     if not any(char.isdigit() for char in s):
#         checks_not_satisfied += 1

#     # Check for consecutive characters.
#     for i in range(1, len(s)):
#         if s[i] == s[i - 1]:
#             checks_not_satisfied += 1
#             break  # We only need to count this once.

#     return checks_not_satisfied

# # Input
# password = input()

# # Check and print the number of checks not satisfied.
# checks = is_valid_password(password)
# print(checks)
