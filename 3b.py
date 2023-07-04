import difflib


def string_similarity(str1, str2):
    result = difflib.SequenceMatcher(None, str1, str2).ratio()
    return result


str1 = input("Enter string1: ")
str2 = input("Enter string 2: ")
match = string_similarity(str1,str2)

print("similarity :", match)