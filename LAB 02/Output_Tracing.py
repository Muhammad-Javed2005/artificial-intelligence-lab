# ==========================================
# Exercise 2 (i) & (ii): Output Tracing
# ==========================================
print("=== Exercise 2 (i): What Would Python Print? ===")
n = 3
print("Tracing Output for loop 1:")
while n >= 0:
    n -= 1
    print(n)
# Explanation: Output will be 2, 1, 0, -1. Loop stops when n becomes -1.

print("\n=== Exercise 2 (ii): Infinite Loop Simulation ===")
# Note: Original code is an infinite loop because n increases (n += 1).
# Demonstrating safely with limit:
n_inf = 4
limit = 0
print("Tracing first 3 iterations of infinite loop (n += 1):")
while n_inf > 0 and limit < 3:
    n_inf += 1
    print(n_inf)
    limit += 1
print("Explanation: Without a break/limit, this runs endlessly because n > 0 remains true.")


# ==========================================
# Exercise 2 (ii) - Subparts 1 to 5: Loop Scenarios
# ==========================================
print("\n=== Exercise 2 (ii).1: Country List ===")
clist = ['Canada', 'USA', 'Mexico', 'Australia']
print("Countries in set:")
for country in clist:
    print(f"- {country}")

print("\n=== Exercise 2 (ii).1: Count 0 to 100 ===")
print("Counting 0 to 100:")
for i in range(101):
    print(i, end=" ")
print()

print("\n=== Exercise 2 (ii).2: Multiplication Table ===")
num = int(input("Enter number for multiplication table: "))
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")

print("\n=== Exercise 2 (ii).3: Numbers 1 to 10 Backwards ===")
for i in range(10, 0, -1):
    print(i, end=" ")
print()

print("\n=== Exercise 2 (ii).4: Even Numbers to 10 ===")
for i in range(0, 11, 2):
    print(i, end=" ")
print()

print("\n=== Exercise 2 (ii).5: Sum Numbers 100 to 200 ===")
total_sum = sum(range(100, 201))
print(f"Sum of numbers from 100 to 200 = {total_sum}")


# ==========================================
# Exercise 2 (iii): While Loop Questions
# ==========================================
print("\n=== Exercise 2 (iii).1: Country List using While Loop ===")
clist_while = ["Canada", "USA", "Mexico"]
idx = 0
while idx < len(clist_while):
    print(f"Country {idx+1}: {clist_while[idx]}")
    idx += 1

print("\n=== Exercise 2 (iii).2: Difference between While and For Loop ===")
diff_text = """
1. For Loop: Iterate karta hai ek fixed sequence (list, range, string) par jab iterations count pata ho.
2. While Loop: Tab tak execute hota hai jab tak given condition TRUE rehti hai (jab iterations count pehle se na pata ho).
"""
print(diff_text)

print("=== Exercise 2 (iii).3: Sum Numbers in a While Loop ===")
s = 0
curr = 1
while curr <= 5:
    s += curr
    curr += 1
print(f"Yes, numbers can be summed in while loop. Example sum (1 to 5) = {s}")

print("\n=== Exercise 2 (iii).4: For Loop inside While Loop ===")
print("Yes, a for loop can easily be nested inside a while loop! Example:")
outer = 1
while outer <= 2:
    print(f"Outer while loop iteration: {outer}")
    for inner in range(1, 3):
        print(f"   Inner for loop value: {inner}")
    outer += 1