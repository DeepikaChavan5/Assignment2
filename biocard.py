# Personal Bio Card in Box Format

# Variables
name = "Deepika Chavan"
age = 21
course = "Artificial Intelligence & Machine Learning"
college = "PES Institute of Technology and Management"
email = "deepikachavan511@gmail.com"

# Card Width
width = 60

print("+" + "-" * (width - 2) + "+")
print("|" + "STUDENT BIO CARD".center(width - 2) + "|")
print("+" + "-" * (width - 2) + "+")

print("| " + f"Name    : {name}".ljust(width - 3) + "|")
print("| " + f"Age     : {age} years".ljust(width - 3) + "|")
print("| " + f"Course  : {course}".ljust(width - 3) + "|")
print("| " + f"College : {college}".ljust(width - 3) + "|")
print("| " + f"Email   : {email}".ljust(width - 3) + "|")

print("+" + "-" * (width - 2) + "+")