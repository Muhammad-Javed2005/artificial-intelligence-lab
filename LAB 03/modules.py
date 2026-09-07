import math
import math as maths
from math import sqrt as squareroot
import time
import glob
import random

# Module Import & Aliasing

print("math.sqrt(9) =", math.sqrt(9))
print("maths.sqrt(16) =", maths.sqrt(16))
print("squareroot(25) =", squareroot(25))

# Time Module

current_time = time.time()
print("\nEpoch Time:", current_time)
print("Human Readable Time:", time.ctime(current_time))
time.sleep(1)

# Glob Module

print("\nAll files:", glob.glob("*"))
print("Python files:", glob.glob("*.py"))

# Random Module

print("\nRandom Int (1-10):", random.randint(1, 10))
print("Random Float:", random.random())
x = [1, 2, 3, 4, 5]
random.shuffle(x)
print("Shuffled List:", x)
print("Random Sample:", random.sample(x, 2))