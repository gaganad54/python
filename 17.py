
# Checks if a word or number is a palindrome

text = input("Enter word/number: ")
#reversing the text
reversed_text = text[::-1]

print("Original:", text)
print("Reversed:", reversed_text)
if text.lower() == reversed_text.lower():
    print("Result: PALINDROME")
else:
    print("Result: NOT A PALINDROME")