input_string = "hai welcome to my channel"
words = input_string.split()  # Split the string into words
smallest_word = min(words, key=len)
longest_word = max(words, key=len)

print(f"The smallest word is: {smallest_word}")
print(f"The longest word is: {longest_word}")
