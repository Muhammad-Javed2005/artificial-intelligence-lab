# Lab Task 05
# Topic: List Comprehensions


# Lab Task 04
# Topic: List Comprehensions

# Part (i): List Comprehension



print("===== Part (i): List Comprehension =====")

words = ["Pakistan", "Apple", "PYTHON", "Karachi", "AI", "Computer", "Hello"]

print("Original List:")
print(words)

# Convert strings having length > 5 into lowercase
lower_words = [word.lower() for word in words if len(word) > 5]

print("\nLowercase Strings (Length > 5):")
print(lower_words)


# Part (ii): Remove 0th, 4th and 5th Elements
# 

print("\n===== Part (ii): Remove Elements =====")

colors = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow', 'Teapink']

print("Original List:")
print(colors)

# Keep only elements except index 0, 4 and 5
new_list = [colors[i] for i in range(len(colors)) if i not in (0, 4, 5)]

print("\nUpdated List:")
print(new_list)