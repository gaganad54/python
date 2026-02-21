
sentence = input("Enter a sentence: ")

# Splitting sentence into words
words = sentence.split()

print("\nOriginal:", sentence)
print("Characters (with spaces):", len(sentence))
print("Characters (without spaces):", len(sentence.replace(" ", "")))
print("Words:", len(words))
print("UPPERCASE:", sentence.upper())
print("lowercase:", sentence.lower())
print("Title Case:", sentence.title())
print("First word:", words[0])
print("Last word:", words[-1])
print("Reversed:", sentence[::-1])