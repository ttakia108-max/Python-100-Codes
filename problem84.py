# Checking Palindrome String
text = input("Enter a string: ")
rev_text = ""
temp = len(text) - 1

while temp >= 0:
    rev_text += text[temp]
    temp -= 1

if text == rev_text:
    print(text, "is a Palindrome")
else:
    print(text, "is NOT a Palindrome")