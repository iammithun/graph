# -*- coding: utf-8 -*-
"""
Created on Tue Feb 27 18:52:59 2024

@author: iamrs
"""

import turtle
import math

# Function to draw Earth
def draw_earth():
    turtle.penup()
    turtle.goto(0, -200)
    turtle.pendown()
    turtle.color('green')
    turtle.begin_fill()
    turtle.circle(200)
    turtle.end_fill()

# Function to draw Moon
def draw_moon():
    turtle.penup()
    turtle.goto(400, 0)
    turtle.pendown()
    turtle.color('pink')
    turtle.begin_fill()
    turtle.circle(50)
    turtle.end_fill()

# Function to draw Chandrayaan-3
def draw_chandrayaan(angle):
    distance_from_earth = 250
    x = distance_from_earth * math.cos(math.radians(angle))
    y = distance_from_earth * math.sin(math.radians(angle))
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.color('blue')
    turtle.begin_fill()
    turtle.circle(10)
    turtle.end_fill()

# Initialize screen and turtle
screen = turtle.Screen()
screen.setup(width=800, height=600)
screen.bgcolor('black')

t = turtle.Turtle()
t.speed(0)

# Animate Chandrayaan-3's orbit around Earth and its movement towards the Moon
for angle in range(0, 360*5, 2):
    t.clear()
    draw_earth()
    draw_moon()
    draw_chandrayaan(angle)
    screen.update()

# Keep the window open
screen.mainloop()
