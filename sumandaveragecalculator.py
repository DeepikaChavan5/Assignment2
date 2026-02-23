# Sum, Average, Median, Mode Calculator

try:
    count = int(input("How many numbers? "))
    
    if count <= 0:
        print("Please enter a positive number!")
    else:
        numbers = []
        total = 0

        for i in range(1, count + 1):
            while True:
                try:
                    num = float(input(f"Enter number {i}: "))
                    numbers.append(num)
                    total += num
                    break
                except ValueError:
                    print("Invalid input! Please enter a number.")

        # Basic Calculations
        maximum = max(numbers)
        minimum = min(numbers)
        average = total / count

        # Median Calculation
        sorted_numbers = sorted(numbers)
        if count % 2 == 1:
            median = sorted_numbers[count // 2]
        else:
            mid1 = sorted_numbers[count // 2 - 1]
            mid2 = sorted_numbers[count // 2]
            median = (mid1 + mid2) / 2

        # Mode Calculation
        frequency = {}
        for num in numbers:
            frequency[num] = frequency.get(num, 0) + 1

        max_freq = max(frequency.values())
        modes = [num for num, freq in frequency.items() if freq == max_freq]

        print("\n=== RESULT ===")
        print(f"Numbers: {numbers}")
        print(f"Sum: {total}")
        print(f"Average: {average}")
        print(f"Maximum: {maximum}")
        print(f"Minimum: {minimum}")
        print(f"Median: {median}")

        if max_freq > 1:
            print(f"Mode: {modes}")
        else:
            print("Mode: No mode (all numbers appear once)")

except ValueError:
    print("Invalid input! Please enter an integer.")