# Lab Task 03
# Question 2: Count Strings

strings = ['abc', 'xyz', 'aba', '1221']

count = 0

for word in strings:
    if len(word) >= 2 and word[0] == word[-1]:
        count += 1

print("List:", strings)
print("Expected Result:", count)