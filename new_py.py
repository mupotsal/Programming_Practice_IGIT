# Author:   TODO: Change this to your names
# Username: TODO: Change this to your usernames
#
# Instructions: Create code that is basketball themed.
# Ask the user for a number of basketballs
# Draw that many basketballs using turtles
#
# A successful student will have completed the following tasks:
# - Task 1: Refactor the code to use a main() function. (6 pts)
# - Task 2: In main(), ask the user to input a number of basketballs to draw, greater than zero. (2 pts)
# - Task 3: If the user enters a number above zero, call the draw_basketballs() function (6 pts)
#   - Otherwise, print another message telling them they aren't good at basketball.
# - Task 4: The draw_basketballs() function is incomplete. (7 pts)
#   - Use a loop to draw the basketballs the correct number of times.
# - Task 5: Add docstrings and comments where appropriate, modify the header block, and clean up any unnecessary code. (4 pts)
####################################################################################
# Submission Instructions:
# Use git to commit and push your changes to the Github repository.
# Make sure your push is complete before the end of class (Section A: 1:10; Section B: 2:30)!

import turtle, random


def setup_window():
    """
    No need to modify this function. It sets up the window and creates a turtle.
    :return: t, a turtle object, and scr, a turtle window
    """
    scr = turtle.Screen()
    t = turtle.Turtle()
    t.speed(0)
    t.fillcolor("chocolate")
    return t, scr


def draw_circle(ness, rad):
    """
    No need to modify this function. It draws the outer circle for the basketball.
    param ness: a turtle object
    param rad: the radius of the circle
    return: None
    """
    ness.left(90)
    ness.begin_fill()
    ness.circle(rad)
    ness.end_fill()


def draw_inner_lines(ness, diameter):
    """
    No need to modify this function. It draws the inner lines of the basketball.
    param ness: a turtle object
    param diameter: the diameter of the circle
    return: None
    """
    ness.right(-45)
    for i in range(2):
        ness.circle(diameter*.707, 90)
        ness.circle(diameter*.707 / 100, 90)
    ness.left(45)
    ness.fd(diameter)


def draw_basketballs(chmad, number_of_basketballs):
    # TODO   This function is incomplete.
    # TODO   Rewrite it to use a loop to create the correct number of basketballs.

    chmad.penup()
    chmad.setpos(random.randint(-250, 250), random.randint(-250, 250))
    chmad.pendown()
    draw_circle(chmad, 100)
    draw_inner_lines(chmad, 200)


# The program starts running here.
mar, w = setup_window()     # sets up the window and a turtle named mar

# TODO   Ask the user to input a number of basketballs to draw.
# TODO   Check if the user entered a number greater than zero.
# TODO   If so, call draw_basketballs() function
# TODO   If not, print a sad basketball-themed message for the user

w.exitonclick()