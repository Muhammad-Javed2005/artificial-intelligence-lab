# Lab Task 04
# Topic: Dictionaries


print("Dictionary Methods")

# Show all dictionary methods
print(dir(dict))

print("\nHelp for dict.get()")
help(dict.get)

print("\nHelp for dict.update() ")
help(dict.update)

# Create a dictionary
student = {
    "name": "Ali",
    "age": 20
}

print("\nOriginal Dictionary:")
print(student)

# get() method
print("\nUsing get()")
print(student.get("name"))

# keys() method
print("\nUsing keys()")
print(student.keys())

# values() method
print("\nUsing values()")
print(student.values())

# items() method
print("\nUsing items()")
print(student.items())

# Add a new key
student["city"] = "Karachi"
print("\nAfter Adding City:")
print(student)

# update() method
student.update({"age": 21})
print("\nAfter update():")
print(student)

# pop() method
student.pop("city")
print("\nAfter pop():")
print(student)

# copy() method
new_student = student.copy()
print("\nCopied Dictionary:")
print(new_student)

# clear() method
temp = {"A": 1, "B": 2}
temp.clear()
print("\nAfter clear():")
print(temp)




print("\n===== Concatenate Dictionaries =====")

dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}

result = {}

result.update(dic1)
result.update(dic2)
result.update(dic3)

print("Dictionary 1:", dic1)
print("Dictionary 2:", dic2)
print("Dictionary 3:", dic3)

print("\nFinal Dictionary:")
print(result)