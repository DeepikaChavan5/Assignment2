# Factorial Calculator
#Input
num = int(input("Enter a number: "))

if num < 0:
    print("Factorial is not defined for negative numbers.")

elif num == 0:
    print("0! = 1")

else:
    factorial = 1
    steps = ""

    for i in range(num, 0, -1):
        factorial *= i
        steps += str(i)
        if i != 1:
            steps += " × "

    print(f"{num}! = {steps} = {factorial}")