import turtle
import random

colors = ["cyan", "light pink", "lemon chiffon", "light yellow", "pale turquoise", "cornsilk", "bisque", "mint cream", "aquamarine", "linen"]

def position(pen, xCoord, yCoord):
    pen.penup()
    pen.goto(xCoord, yCoord)
    pen.pendown()


def generate_random():
    return random.randint(-300, 300)


def draw_star(pen, radius, num_points, pen_color_1, pen_color_2):
    
    pen.color(pen_color_1)
    for _ in range(num_points):
        pen.forward(radius)
        pen.backward(radius)
        pen.right(360 / num_points)
    
    pen.color(pen_color_2)
    pen.right(5)
    for _ in range(num_points):
        pen.forward(radius /2 )
        pen.backward(radius /2)
        pen.right(360 / num_points)


def draw_4pt_star(pen, radius, pen_color):
    pen.color(pen_color)
    pen.begin_fill()

    for _ in range(4):
        pen.circle(radius, 90)
        pen.right(180)
    
    pen.end_fill()


def draw_8pt_star(pen, radius, pen_color):
    draw_4pt_star(pen, radius, pen_color)
    pen.left(50)
    pen.penup()
    pen.forward(radius * 0.65)
    pen.right(90)
    draw_4pt_star(pen, radius, pen_color)


def goto_and_draw_4pt(my_turtle, radius, pen_color):
    position(my_turtle, generate_random(), generate_random())
    draw_4pt_star(my_turtle, radius, pen_color)


def draw_many_stars(my_turtle):
    for i in range(10):
        for j in range(1,5):

            for _ in range(4):
                goto_and_draw_4pt(my_turtle, j, colors[i])

            position(my_turtle, generate_random(), generate_random())
            draw_8pt_star(my_turtle, j, colors[i])



# The following functions draw the stars in the libra constellation,
# with as accurate as possible sizes, colors, and positions.

# Some of the stars in the constellation have names beginning with the zuben prefix,
# and some of them do not have proper names and are referred to by the greek letters
# theta, tau, and upsilon, followed by 'librae' to denote that these lesser stars
# belong to the libra constellation.

def draw_theta_librae(pen):
    position(pen, -75, -80)
    draw_star(pen, 10, 20, "sandy brown", "moccasin")

def draw_zubenelakrab(pen):
    position(pen, -90, 10)
    draw_star(pen, 12, 25, "orange", "moccasin")

def draw_zubeneschamali(pen):
    position(pen, -180, 150)
    draw_star(pen, 24, 32, "blue", "light sky blue")

def draw_zubenelgenubi(pen):
    position(pen, -10, 250)
    draw_star(pen, 20, 30, "medium blue", "light sky blue")

def draw_brachium(pen):
    position(pen, 180, 140)
    draw_star(pen, 18, 25, "dark orange", "orange")

def draw_upsilon_librae(pen):
    position(pen, 205, -50)
    draw_star(pen, 12, 25, "orange", "moccasin")

def draw_tau_librae(pen):
    position(pen, 220, -60)
    draw_star(pen, 14, 25, "midnight blue", "cornflower blue")

def draw_libra_constellation(my_turtle):
    draw_theta_librae(my_turtle)
    draw_zubenelakrab(my_turtle)
    draw_zubeneschamali(my_turtle)
    draw_zubenelgenubi(my_turtle)
    draw_brachium(my_turtle)
    draw_upsilon_librae(my_turtle)
    draw_tau_librae(my_turtle)     




def draw_night_sky():

    wn = turtle.Screen()
    wn.bgcolor('#03012b')
    my_turtle = turtle.Turtle()
    my_turtle.speed(0)
    my_turtle.pensize(1)

    draw_many_stars(my_turtle)

    draw_libra_constellation(my_turtle)

    wn.exitonclick()

draw_night_sky()
