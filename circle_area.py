import math

radius = float(input("Enter the radius of the circle: "))

radius_squared = radius * radius
area = math.pi * radius_squared

print(f"The area of the circle is {area:.2f}")
