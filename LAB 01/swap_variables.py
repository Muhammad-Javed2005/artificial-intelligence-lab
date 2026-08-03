# Lab Task 01
# Question 1: Swap Four Variables

a = int(input("Enter value for a: "))
b = int(input("Enter value for b: "))
c = int(input("Enter value for c: "))
d = int(input("Enter value for d: "))


print("\Before Swapping")
print(f"a = {a}, b = {b}, c = {c}, d = {d}")

a , b , c , d = d , c , b , a


print("\nAfter Swapping")
print(f"a = {a}, b = {b}, c = {c}, d = {d}")
