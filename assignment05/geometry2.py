import math
def area_circle(radius):
    return math.pi * radius * radius
def area_rectangle(length, width):
    return length * width
from geometry import area_circle, area_rectangle
print("Area Calculator")
print("1. Area of Circle")
print("2. Area of Rectangle")
choice = int(input("Enter your choice (1 or 2): "))
if choice == 1:
    r = float(input("Enter radius of the circle: "))
    area = area_circle(r)
    print("Area of circle:", area)
elif choice == 2:
    l = float(input("Enter length of the rectangle: "))
    w = float(input("Enter width of the rectangle: "))
    area = area_rectangle(l, w)
    print("Area of rectangle:", area)
else:
    print("Invalid choice")