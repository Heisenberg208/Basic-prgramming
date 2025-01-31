sentence = input("Enter a sentence: ")

word_count = len(sentence.split())
digit_count = sum(char.isdigit() for char in sentence)
uppercase_count = sum(char.isupper() for char in sentence)
lowercase_count = sum(char.islower() for char in sentence)

print("Number of words:", word_count)
print("Number of digits:", digit_count)
print("Number of uppercase letters:", uppercase_count)
print("Number of lowercase letters:", lowercase_count)
