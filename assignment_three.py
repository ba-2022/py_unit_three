# Betelhem Alemu
# 10/20/22
# This program creates a hexagon flower

import turtle

# This function asks the user for a side length
def get_side_length():
    return float(input("Enter a side length:"))

# This functions asks the user for a center color
def get_center_color():
    return str(input("Enter the color of the center:"))

# This functions asks the user for the petal colors
def get_petal_color():
    return str(input("Enter the color of the petals:"))

''' This function creates the flower
'''
def draw_a_flower(size, center, petal,):

    draw_a_hexagon(size,center)
    turtle.forward(size)
    turtle.left(180)
    for x in range(6):
        draw_a_hexagon(size, petal)
        turtle.forward(size)
        turtle.left(60)

'''This functions creates the hexagon, which is the shape of the flower being drawn
'''
def draw_a_hexagon(size, color):
    turtle.begin_fill()
    turtle.fillcolor(color)
    for x in range(6):
        turtle.forward(size)
        turtle.left(300)
    turtle.end_fill()

'''This function calls the other functions
'''
def main():
    sideLength = get_side_length()
    centerColor = get_center_color()
    petalColor = get_petal_color()

    draw_a_flower(sideLength, centerColor, petalColor)

main()



turtle.exitonclick()
