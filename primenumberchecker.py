# Prime Number Checker

# ---------- PART 1: Single Number Check ----------

num = int(input("Enter a number: "))

if num < 0:
    print(f"{num} is NOT a prime number (Negative numbers are not prime).")

elif num == 0 or num == 1:
    print(f"{num} is NOT a prime number.")

elif num == 2:
    print("2 is a PRIME number.")

else:
    is_prime = True
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            is_prime = False
            break

    if is_prime:
        print(f"{num} is a PRIME number.")
    else:
        print(f"{num} is NOT a prime number.")


# ---------- PART 2: Prime Numbers in a Range ----------

start = int(input("\nEnter start range: "))
end = int(input("Enter end range: "))

print("Prime numbers:", end=" ")

prime_list = []

for number in range(start, end + 1):
    if number > 1:
        for i in range(2, int(number**0.5) + 1):
            if number % i == 0:
                break
        else:
            prime_list.append(number)

print(", ".join(map(str, prime_list)))