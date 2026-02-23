# TEXT ANALYSIS FUNCTIONS

# 1. Count Words
def count_words(text):
    words = text.split()
    return len(words)

# 2. Count Vowels
def count_vowels(text):
    vowels = "aeiouAEIOU"
    count = 0
    for char in text:
        if char in vowels:
            count += 1
    return count

# 3. Count Consonants
def count_consonants(text):
    vowels = "aeiouAEIOU"
    count = 0
    for char in text:
        if char.isalpha() and char not in vowels:
            count += 1
    return count

# 4. Reverse Text
def reverse_text(text):
    return text[::-1]

# 5. Check Palindrome
def is_palindrome(text):
    cleaned = text.replace(" ", "").lower()
    return cleaned == cleaned[::-1]

# 6. Remove Vowels
def remove_vowels(text):
    vowels = "aeiouAEIOU"
    result = ""
    for char in text:
        if char not in vowels:
            result += char
    return result

# 7. Word Frequency
def word_frequency(text):
    words = text.lower().split()
    freq = {}
    for word in words:
        freq[word] = freq.get(word, 0) + 1
    return freq

# 8. Longest Word
def longest_word(text):
    words = text.split()
    longest = ""
    for word in words:
        if len(word) > len(longest):
            longest = word
    return longest

# 9. Analyze Text (Main Function)
def analyze_text(text):
    print("\n=== TEXT ANALYSIS ===")

    print("Words:", count_words(text))
    print("Vowels:", count_vowels(text))
    print("Consonants:", count_consonants(text))
    print("Reversed:", reverse_text(text))

    if is_palindrome(text):
        print("Palindrome: Yes")
    else:
        print("Palindrome: No")

    print("Without vowels:", remove_vowels(text))

    longest = longest_word(text)
    print(f"Longest word: {longest} ({len(longest)} letters)")

    freq = word_frequency(text)
    print("Word Frequency:")
    for word, count in freq.items():
        print(f"{word}: {count}")

# ----------- MAIN PROGRAM -----------
user_text = input("Enter text: ")
analyze_text(user_text)