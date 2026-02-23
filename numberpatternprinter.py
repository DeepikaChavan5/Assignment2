# Number Pattern Printer (Updated with 7 Patterns)

while True:
    print("\n=== NUMBER PATTERN PRINTER ===")
    print("1. Pattern 1 (Increasing Numbers)")
    print("2. Pattern 2 (Repeated Numbers)")
    print("3. Pattern 3 (Reverse Triangle)")
    print("4. Pattern 4 (Pyramid Numbers)")
    print("5. Pattern 5 (Right-Aligned Triangle)")
    print("6. Pattern 6 (Floyd’s Triangle)")
    print("7. Pattern 7 (Diamond Pattern)")
    print("8. Exit")

    choice = input("Choose pattern (1-8): ")

    if choice == "8":
        print("Exiting program... Goodbye!")
        break

    if choice not in [str(i) for i in range(1, 8)]:
        print("Invalid choice! Please select between 1-8.")
        continue

    try:
        height = int(input("Enter height: "))
        if height <= 0:
            print("Height must be positive!")
            continue
    except ValueError:
        print("Please enter a valid number!")
        continue

    print("\n--- Pattern Output ---")

    # Pattern 1
    if choice == "1":
        for i in range(1, height + 1):
            for j in range(1, i + 1):
                print(j, end=" ")
            print()

    # Pattern 2
    elif choice == "2":
        for i in range(1, height + 1):
            for j in range(i):
                print(i, end=" ")
            print()

    # Pattern 3
    elif choice == "3":
        for i in range(height, 0, -1):
            for j in range(i, 0, -1):
                print(j, end=" ")
            print()

    # Pattern 4
    elif choice == "4":
        for i in range(1, height + 1):
            for j in range(1, i + 1):
                print(j, end="")
            for j in range(i - 1, 0, -1):
                print(j, end="")
            print()

    # Pattern 5 (Right-Aligned Triangle)
    elif choice == "5":
        for i in range(1, height + 1):
            print("  " * (height - i), end="")
            for j in range(1, i + 1):
                print(j, end=" ")
            print()

    # Pattern 6 (Floyd’s Triangle)
    elif choice == "6":
        num = 1
        for i in range(1, height + 1):
            for j in range(i):
                print(num, end=" ")
                num += 1
            print()

    # Pattern 7 (Diamond Pattern)
    elif choice == "7":
        # Upper part
        for i in range(1, height + 1):
            print(" " * (height - i), end="")
            for j in range(1, i + 1):
                print(j, end="")
            for j in range(i - 1, 0, -1):
                print(j, end="")
            print()

        # Lower part
        for i in range(height - 1, 0, -1):
            print(" " * (height - i), end="")
            for j in range(1, i + 1):
                print(j, end="")
            for j in range(i - 1, 0, -1):
                print(j, end="")
            print()