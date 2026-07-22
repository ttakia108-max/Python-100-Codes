# Checking Sentence Palindrome (Ignoring Spaces)
text = input("Enter a sentence: ").lower()
text = text.replace(" ", "")
rev_text = text[::-1]

if text == rev_text:
    print("It is a Palindrome")
else:
    print("It is NOT a Palindrome")