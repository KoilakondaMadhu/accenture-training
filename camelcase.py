# Define a function named camelcase that takes a list of words as input
def camelcase(list_words):
    # Convert each word to camel case
    # by making the first letter uppercase and the rest lowercase
    converted = "".join(word[0].upper() + word[1:].lower() for word in list_words)

    # Make the first letter of the concatenated string lowercase
    # and concatenate it with the rest of the string
    return converted[0].lower() + converted[1:]

# Define a list of words
words = ["Hello", "Welcome", "To", "Python", "Programming", "In", "Javatpoint"]

# Call the camelcase function and print the result
print(camelcase(words))
