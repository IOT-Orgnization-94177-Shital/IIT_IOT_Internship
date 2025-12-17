import math
def area_circle(radius):
    """Calculate area of a circle"""
    return math.pi * radius * radius
def area_rectangle(length, width):
    """Calculate area of a rectangle"""
    return length * width
import geometry
r = 5
print("Area of circle:", geometry.area_circle(r))
l = 10
w = 4
print("Area of rectangle:", geometry.area_rectangle(l, w))