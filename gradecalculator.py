# Grade Calculator Program

# Taking marks input
print("Enter marks for 5 subjects (out of 100):")

sub1 = float(input("Subject 1: "))
sub2 = float(input("Subject 2: "))
sub3 = float(input("Subject 3: "))
sub4 = float(input("Subject 4: "))
sub5 = float(input("Subject 5: "))

# Total and Percentage
total = sub1 + sub2 + sub3 + sub4 + sub5
percentage = (total / 500) * 100

# Grade Calculation
if percentage >= 90:
    grade = "A+ (Outstanding)"
elif percentage >= 80:
    grade = "A (Excellent)"
elif percentage >= 70:
    grade = "B (Good)"
elif percentage >= 60:
    grade = "C (Average)"
elif percentage >= 50:
    grade = "D (Pass)"
else:
    grade = "F (Fail)"

# Pass/Fail Condition (All subjects >= 40)
if sub1 >= 40 and sub2 >= 40 and sub3 >= 40 and sub4 >= 40 and sub5 >= 40:
    result = "Pass"
else:
    result = "Fail"

# Display Output
print("\n=== RESULT SUMMARY ===")
print(f"Subject 1: {sub1}")
print(f"Subject 2: {sub2}")
print(f"Subject 3: {sub3}")
print(f"Subject 4: {sub4}")
print(f"Subject 5: {sub5}")
print(f"Total Marks: {total} / 500")
print(f"Percentage: {percentage:.2f}%")
print(f"Grade: {grade}")
print(f"Result: {result}")