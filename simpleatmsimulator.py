# Simple ATM Simulator with Transaction History

balance = 10000   # Initial Balance
MIN_BALANCE = 500
transactions = []   # List to store transaction history

while True:
    print("\n=== ATM SIMULATOR ===")
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Transaction History")
    print("5. Exit")

    choice = input("Enter choice (1-5): ")

    # Check Balance
    if choice == "1":
        print(f"Current Balance: ₹{balance:.2f}")

    # Deposit
    elif choice == "2":
        try:
            amount = float(input("Enter amount to deposit: ₹"))
            if amount > 0:
                balance += amount
                transactions.append(f"Deposited ₹{amount:.2f}")
                print("Deposit successful!")
                print(f"Updated Balance: ₹{balance:.2f}")
            else:
                print("Invalid deposit amount!")
        except ValueError:
            print("Please enter a valid number!")

    # Withdraw
    elif choice == "3":
        try:
            amount = float(input("Enter amount to withdraw: ₹"))

            if amount <= 0:
                print("Invalid withdrawal amount!")

            elif amount > balance:
                print("Insufficient balance!")

            elif balance - amount < MIN_BALANCE:
                print(f"Minimum balance of ₹{MIN_BALANCE} must be maintained.")
                print(f"Available for withdrawal: ₹{balance - MIN_BALANCE:.2f}")

            else:
                balance -= amount
                transactions.append(f"Withdrew ₹{amount:.2f}")
                print("Withdrawal successful!")
                print(f"New Balance: ₹{balance:.2f}")

        except ValueError:
            print("Please enter a valid number!")

    # Transaction History
    elif choice == "4":
        print("\n=== TRANSACTION HISTORY ===")
        if not transactions:
            print("No transactions yet.")
        else:
            for i, t in enumerate(transactions, 1):
                print(f"{i}. {t}")
        print(f"Current Balance: ₹{balance:.2f}")

    # Exit
    elif choice == "5":
        print("Thank you for using ATM. Goodbye!")
        break

    else:
        print("Invalid choice! Please select between 1-5.")