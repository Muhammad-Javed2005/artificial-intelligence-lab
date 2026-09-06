import datetime

# Task I: Square and Cube using Lambda
numbers = [1, 2, 3, 4, 5]
squares = list(map(lambda x: x**2, numbers))
cubes = list(map(lambda x: x**3, numbers))

print("Original List:", numbers)
print("Squared List:", squares)
print("Cubed List:", cubes)

# Task II: String Start-Character Check
starts_with = lambda string, char: string.lower().startswith(char.lower())
test_str = "Python"
test_char = "P"
print(f"Does '{test_str}' start with '{test_char}'? -> {starts_with(test_str, test_char)}")

# Task III: Extract Year, Month, Date, Time
now = datetime.datetime.now()
get_year = lambda dt: dt.year
get_month = lambda dt: dt.month
get_day = lambda dt: dt.day
get_time = lambda dt: dt.strftime("%H:%M:%S")

print("Current Datetime:", now)
print("Year:", get_year(now))
print("Month:", get_month(now))
print("Day:", get_day(now))
print("Time:", get_time(now))