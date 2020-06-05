"""
File: pyramid.py
----------------
YOUR DESCRIPTION HERE
"""

import tkinter
import time
import numpy as np

CANVAS_WIDTH = 600  # Width of drawing canvas in pixels
CANVAS_HEIGHT = 600  # Height of drawing canvas in pixels
x0 = 10
y0 = 7

x = 5
y = 8

BALL_SIZE = 70

top = tkinter.Tk()
top.minsize(width=600, height=600)
top.title('Elastic Collision')
canvas = tkinter.Canvas(top, width=600, height=600)
canvas.pack()

ball = canvas.create_oval(0, 0, BALL_SIZE, BALL_SIZE, fill='blue', outline='blue')
ball2 = canvas.create_oval(80, 80, 150, 150, fill='yellow', outline='yellow')

dx0 = x0
dy0 = y0

dx1 = x
dy1 = y

def get_coordinates(item):
    x1 = canvas.coords(item)[0]
    y1 = canvas.coords(item)[1]
    x2 = canvas.coords(item)[2]
    y2 = canvas.coords(item)[3]

    p = []

    p0 = [x1, y1]
    p1 = [x1 + 35, y1]
    p2 = [x1 + 70, y1]
    p3 = [x1, y1 + 35]
    p4 = [x2, y2 - 35]
    p5 = [x2 - 70, y2]
    p6 = [x2 - 35, y2]
    p7 = [x2, y2]

    p.extend([p0, p1, p2, p3, p4, p5, p6, p7])

    return p

def detect_collision(item1, item2):
    c1 = get_coordinates(item1)
    c2 = get_coordinates(item2)

    if c1[2] <= c2[0] <= c1[7]:
        print("Collision")
        return True
    elif c1[0] <= c2[2] <= c1[5]:
        print("Collision")
        return True
    elif c1[5] <= c2[1] <= c1[7]:
        print("Collision")
        return True
    elif c1[0] <= c2[6] <= c1[2]:
        print("Collision")
        return True


def hit_left_wall(canvas, object):
    return get_left_x(canvas, object) <= 0


def hit_top_wall(canvas, object):
    return get_top_y(canvas, object) <= 0


def hit_right_wall(canvas, object):
    return get_right_x(canvas, object) >= CANVAS_WIDTH


def hit_bottom_wall(canvas, object):
    return get_bottom_y(canvas, object) >= CANVAS_HEIGHT


######## These helper methods use "lists" ###########
### Which is a concept you will learn Monday ###########

def get_left_x(canvas, object):
    return canvas.coords(object)[0]


def get_top_y(canvas, object):
    return canvas.coords(object)[1]


def get_right_x(canvas, object):
    return canvas.coords(object)[2]


def get_bottom_y(canvas, object):
    return canvas.coords(object)[3]


while True:
    # update world
    canvas.move(ball, dx0, dy0)
    canvas.move(ball2, dx1, dy1)

    if hit_left_wall(canvas, ball) or hit_right_wall(canvas, ball):
        dx0 *= -1
    if hit_left_wall(canvas, ball2) or hit_right_wall(canvas, ball2):
        dx1 *= -1
    if hit_top_wall(canvas, ball) or hit_bottom_wall(canvas, ball):
        dy0 *= -1
    if hit_top_wall(canvas, ball2) or hit_bottom_wall(canvas, ball2):
        dy1 *= -1

    if detect_collision(ball, ball2):
        dx0 *= -1
        dy0 *= -1

    # redraw canvas
    canvas.update()
    # pause
    time.sleep(1 / 50.)


