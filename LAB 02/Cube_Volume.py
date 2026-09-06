# ==========================================
# Exercise 1 (i): Cube Volume & Category
# ==========================================
print("=== Exercise 1 (i): Cube Volume Category ===")
height = float(input("Enter height (cm): "))
width = float(input("Enter width (cm): "))
depth = float(input("Enter depth (cm): "))

volume = height * width * depth
print(f"Calculated Volume: {volume:.2f} cm³")

if 1 <= volume <= 10:
    label = "Extra Small"
elif 11 <= volume <= 25:
    label = "Small"
elif 26 <= volume <= 75:
    label = "Medium"
elif 76 <= volume <= 100:
    label = "Large"
elif 101 <= volume <= 250:
    label = "Extra Large"
elif volume >= 251:
    label = "Extra-Extra Large"
else:
    label = "Below Range / Invalid Volume"

print(f"Label: {label}")


# ==========================================
# Exercise 1 (ii): Worker Efficiency
# ==========================================
print("\n=== Exercise 1 (ii): Worker Efficiency ===")
time_taken = float(input("Enter time taken by worker (in hours): "))

if 2 <= time_taken <= 3:
    print("Efficiency Status: Highly Efficient")
elif 3 < time_taken <= 4:
    print("Efficiency Status: Ordered to improve speed")
elif 4 < time_taken <= 5:
    print("Efficiency Status: Given training to improve speed")
elif time_taken > 5:
    print("Efficiency Status: Worker has to leave the company")
else:
    print("Time taken is less than 2 hours (Invalid/Exceptional).")


# ==========================================
# Exercise 1 (iii): Case-Insensitive Password
# ==========================================
print("\n=== Exercise 1 (iii): Password Verification ===")
username = input("Enter username: ")
password = input("What is the password? ")

# Known password (abc$123 / ABC$123)
if password.lower() == "abc$123":
    print("Welcome!")
else:
    print("I don't know you.")