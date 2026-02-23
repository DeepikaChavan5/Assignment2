# Leap Year Checker Program

year = int(input("Enter a year: "))

# Leap year condition
if (year % 4 == 0) and (year % 100 != 0 or year % 400 == 0):
    print("\n=== RESULT ===")
    print(f"{year} is a Leap Year.")
    
    if year % 400 == 0:
        print("Reason: It is divisible by 400.")
    elif year % 100 == 0:
        print("Reason: It is divisible by 100 but also divisible by 400.")
    else:
        print("Reason: It is divisible by 4 and not divisible by 100.")
else:
    print("\n=== RESULT ===")
    print(f"{year} is NOT a Leap Year.")
    
    if year % 4 != 0:
        print("Reason: It is not divisible by 4.")
    elif year % 100 == 0 and year % 400 != 0:
        print("Reason: It is divisible by 100 but not divisible by 400.")