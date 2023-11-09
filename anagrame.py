s1 = input("Enter the first string: ").lower().replace(" ", "")
s2 = input("Enter the second string: ").lower().replace(" ", "")

# Sort the characters of both strings
sorted_s1 = sorted(s1)
sorted_s2 = sorted(s2)

if sorted_s1 == sorted_s2:
    print('Anagram')
else:
    print("Not an anagram")
