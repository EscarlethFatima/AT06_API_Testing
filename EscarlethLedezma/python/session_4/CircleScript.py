import CircleArea as area
import CirclePerimeter as perimeter

# This script is to return the calculate the area and perimeter of a circle

radius = int(input('Enter the circle radius:'))
print('The circle area is:', area.circle_area(radius))
print('The circle perimeter is:', perimeter.circle_perimeter(radius))
