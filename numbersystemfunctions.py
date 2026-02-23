# NUMBER SYSTEM FUNCTIONS

# 1. Factorial
def factorial(n):
    if n < 0:
        return "Factorial not defined for negative numbers"
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

# 2. Prime Check
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

# 3. Fibonacci (nth number)
def fibonacci(n):
    if n <= 0:
        return "Enter positive position"
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    a, b = 0, 1
    for _ in range(3, n + 1):
        a, b = b, a + b
    return b

# 4. Sum of Digits
def sum_of_digits(n):
    return sum(int(digit) for digit in str(abs(n)))

# 5. Reverse Number
def reverse_number(n):
    sign = -1 if n < 0 else 1
    reversed_num = int(str(abs(n))[::-1])
    return sign * reversed_num

# 6. Armstrong Number
def is_armstrong(n):
    num_str = str(abs(n))
    power = len(num_str)
    total = sum(int(digit) ** power for digit in num_str)
    return total == abs(n)

# 7. GCD (Euclidean Algorithm)
def gcd(a, b):
    while b:
        a, b = b, a % b
    return abs(a)

# 8. LCM
def lcm(a, b):
    if a == 0 or b == 0:
        return 0
    return abs(a * b) // gcd(a, b)

# 9. Perfect Number
def is_perfect_number(n):
    if n <= 1:
        return False
    divisors_sum = 1
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            divisors_sum += i
            if i != n // i:
                divisors_sum += n // i
    return divisors_sum == n

# 10. Menu Function
def math_menu():
    while True:
        print("\n=== NUMBER SYSTEM MENU ===")
        print("1. Factorial")
        print("2. Prime Check")
        print("3. Fibonacci")
        print("4. Sum of Digits")
        print("5. Reverse Number")
        print("6. Armstrong Number")
        print("7. GCD")
        print("8. LCM")
        print("9. Perfect Number")
        print("10. Exit")

        choice = input("Enter choice (1-10): ")

        if choice == "10":
            print("Exiting Program...")
            break

        try:
            if choice == "1":
                n = int(input("Enter number: "))
                print("Factorial:", factorial(n))

            elif choice == "2":
                n = int(input("Enter number: "))
                print("Prime:" if is_prime(n) else "Not Prime")

            elif choice == "3":
                n = int(input("Enter position (n): "))
                print("Fibonacci:", fibonacci(n))

            elif choice == "4":
                n = int(input("Enter number: "))
                print("Sum of digits:", sum_of_digits(n))

            elif choice == "5":
                n = int(input("Enter number: "))
                print("Reversed number:", reverse_number(n))

            elif choice == "6":
                n = int(input("Enter number: "))
                print("Armstrong:" if is_armstrong(n) else "Not Armstrong")

            elif choice == "7":
                a = int(input("Enter first number: "))
                b = int(input("Enter second number: "))
                print("GCD:", gcd(a, b))

            elif choice == "8":
                a = int(input("Enter first number: "))
                b = int(input("Enter second number: "))
                print("LCM:", lcm(a, b))

            elif choice == "9":
                n = int(input("Enter number: "))
                print("Perfect Number:" if is_perfect_number(n) else "Not Perfect")

            else:
                print("Invalid choice! Please select 1-10.")

        except ValueError:
            print("Invalid input! Please enter integers only.")

# Run the program
math_menu()