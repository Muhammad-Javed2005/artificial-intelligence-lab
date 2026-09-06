# Task I: Store City Details
num_cities = int(input("How many cities do you want to enter? "))

with open("cities.txt", "w") as file:
    for i in range(num_cities):
        print(f"\nEntering details for City {i + 1}:")
        name = input("City Name: ")
        population = input("Population: ")
        mayor = input("Mayor Name: ")
        file.write(f"City: {name}, Population: {population}, Mayor: {mayor}\n")

print("\nCity data saved to 'cities.txt'.")

# Task II: Append to student.txt
with open("student.txt", "a") as file:
    file.write("Now we are AI students\n")

print("Message appended to 'student.txt'.")

with open("student.txt", "r") as file:
    print("\nContent of 'student.txt':")
    print(file.read())