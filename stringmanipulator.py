# String Manipulator Program

# Taking input from user
sentence = input("Enter a sentence: ")

# Calculations
total_chars_with_spaces = len(sentence)
total_chars_without_spaces = len(sentence.replace(" ", ""))
words = sentence.split()
total_words = len(words)
uppercase = sentence.upper()
lowercase = sentence.lower()
title_case = sentence.title()
first_word = words[0] if total_words > 0 else ""
last_word = words[-1] if total_words > 0 else ""
reversed_sentence = sentence[::-1]

# Displaying results
print("\nOriginal:", sentence)
print("Characters (with spaces):", total_chars_with_spaces)
print("Characters (without spaces):", total_chars_without_spaces)
print("Words:", total_words)
print("UPPERCASE:", uppercase)
print("lowercase:", lowercase)
print("Title Case:", title_case)
print("First word:", first_word)
print("Last word:", last_word)
print("Reversed:", reversed_sentence)