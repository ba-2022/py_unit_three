# Betelhem Alemu
# 10/18/22
# This program creates a hexagon flower

import turtle

''' This function asks the user for a side length'''
get_side_length = int(input("Please enter a side length"))


''' This function asks the user for a color for the center of the flower'''
get_center_color = str(input("Please enter a color for the center"))

''' This function asks the user for the flowers petal color'''
get_petal_color = input("Please enter a color for the petal")

movement = get_side_length * -2

# this function calls for the drawing of the hehxagon
def draw_flower(color):
        turtle.fillcolor(color)
        turtle.begin_fill()
        for x in range(6):
            turtle.forward(get_side_length)
            turtle.pendown()
            turtle.left(60)
        turtle.end_fill()

# this function draws the center of the flower and fills in the color inputed by the user
def draw_center(color):
    turtle.right(60)
    turtle.left(60)
    turtle.forward(movement)
    draw_flower(get_center_color)


# this function draws the petals of the flower and fills in the color inputed by the user
def draw_petal():
    for x in range(5):
        turtle.forward(get_side_length)
        turtle.right(60)
        draw_flower(get_petal_color)


def main():
    draw_flower(get_petal_color)
    draw_petal()
    draw_center(get_center_color)





main()

'''
after running the code, this function lets the screen stay open
until you click on exit
'''

turtle.exitonclick()