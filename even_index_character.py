# Ask user
user_input = input("Enter a string: ")

# Display characters at even index numbers
word = list(user_input)
for i in word[0::2]:
    print(i)