# Movie Ticket Pricing System

# User Inputs
age = int(input("Enter age: "))
day = input("Enter day of week: ").strip().lower()
tickets = int(input("Enter number of tickets: "))

# Age-based Pricing
if age < 3:
    base_price = 0
    category = "Free"
elif 3 <= age <= 12:
    base_price = 150
    category = "Child"
elif 13 <= age <= 59:
    base_price = 300
    category = "Adult"
else:
    base_price = 200
    category = "Senior"

# Discount Calculation
if day in ["friday", "saturday", "sunday"]:
    discount_percent = 20
else:
    discount_percent = 0

# Calculations
subtotal = base_price * tickets
discount_amount = (subtotal * discount_percent) / 100
final_amount = subtotal - discount_amount

# Display Output
print("\n=== TICKET BILL DETAILS ===")
print(f"Category: {category}")
print(f"Base price per ticket: ₹{base_price:.2f}")
print(f"Number of tickets: {tickets}")
print(f"Subtotal: ₹{subtotal:.2f}")
print(f"Discount ({discount_percent}%): -₹{discount_amount:.2f}")
print(f"Final Amount: ₹{final_amount:.2f}")