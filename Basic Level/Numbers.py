# 1. Format function with 145 and 'o'
def format_number(num, spec):
    return format(num, spec)
print(format_number(145, 'o'))  # Outputs 221 (octal representation)

# 2. Pond area and water volume
radius = 84
pi = 3.14
area = pi * radius * radius
water_per_sqm = 1.4
total_water = area * water_per_sqm
print(int(total_water))  # Outputs 31018

# 3. Speed calculation
distance = 490
time_minutes = 7
time_seconds = time_minutes * 60
speed = distance / time_seconds
print(int(speed))  # Outputs 1