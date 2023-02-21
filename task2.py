# area of the foundation of a building
import math

building_shape = input('is the building  a : "square", "rectangle", or "round"')

if building_shape == "square":
    length_square = int(input("Enter the length of the building:"))
    area_of_square = length_square * length_square
    print(f"Area of square foundation is : {area_of_square} ")

elif building_shape == "rectangle":
    length_rectangle = float(input("Enter the length  of rectangle:"))
    width_rectangle = float(input("Enter the width of rectangle:"))
    area_of_rectangle = length_rectangle * width_rectangle
    print(f"The area of rectangle foundation is: {area_of_rectangle}")

else:
    building_shape == "round"
    circle_radius = float(input("Enter the radius of the circle:"))
    round_area = 3.14 * circle_radius * circle_radius   # this assumes the value of Pi = 3.14
    print(f"The foundation area of the circle is: {round_area}")
