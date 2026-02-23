# Palindrome Checker

value = input("Enter word/number: ")

# Step 1: Store original value
original = value

# Step 2: Convert to lowercase for checking (ignore case)
processed = value.lower()

# Step 3: Reverse the value
reversed_value = processed[::-1]

# Display Steps
print("\n--- Verification Steps ---")
print("Original:", original)
print("Lowercase for checking:", processed)
print("Reversed:", reversed_value)

# Step 4: Check palindrome
if processed == reversed_value:
    print("Result: PALINDROME")
else:
    print("Result: NOT A PALINDROME")