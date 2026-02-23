# Temperature Converter Program

while True:
    print("\n=== TEMPERATURE CONVERTER ===")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    print("3. Celsius to Kelvin")
    print("4. Kelvin to Celsius")
    print("5. Fahrenheit to Kelvin")
    print("6. Kelvin to Fahrenheit")
    print("7. Exit")

    choice = int(input("Enter your choice (1-7): "))

    if choice == 7:
        print("Exiting program... Goodbye!")
        break

    if choice >= 1 and choice <= 6:
        temp = float(input("Enter temperature value: "))

        if choice == 1:
            result = (temp * 9/5) + 32
            print(f"{temp}°C = {result:.2f}°F")

        elif choice == 2:
            result = (temp - 32) * 5/9
            print(f"{temp}°F = {result:.2f}°C")

        elif choice == 3:
            result = temp + 273.15
            print(f"{temp}°C = {result:.2f}K")

        elif choice == 4:
            result = temp - 273.15
            print(f"{temp}K = {result:.2f}°C")

        elif choice == 5:
            result = (temp - 32) * 5/9 + 273.15
            print(f"{temp}°F = {result:.2f}K")

        elif choice == 6:
            result = (temp - 273.15) * 9/5 + 32
            print(f"{temp}K = {result:.2f}°F")

    else:
        print("Invalid choice! Please select between 1 and 7.")