import turtle
import math
import time

screen = turtle.Screen()
screen.setup(700, 700)
screen.bgcolor("black")
screen.colormode(1.0)
screen.tracer(0)

t = turtle.Turtle()
t.hideturtle()
t.speed(0)


def heart_x(angle):
    return 16 * (math.sin(angle) ** 3)


def heart_y(angle):
    return 13 * math.cos(angle) - 5 * math.cos(2 * angle) - 2 * math.cos(3 * angle) - math.cos(4 * angle)


N = 200
outer_scale = 18.0
inner_scale = 5.0
steps = 20

c_outer = (1.0, 0.70, 0.78)
c_inner = (0.0, 0.0, 0.0)

for i in range(N):
    angle = 2 * math.pi * i / N
    hx, hy = heart_x(angle), heart_y(angle)

    ox, oy = hx * outer_scale, hy * outer_scale
    ix, iy = hx * inner_scale, hy * inner_scale

    for j in range(steps + 1):
        f = j / steps
        x = ox + (ix - ox) * f
        y = oy + (iy - oy) * f
        color = tuple(c_outer[k] + (c_inner[k] - c_outer[k]) * f for k in range(3))

        t.penup()
        t.goto(x, y)
        t.pendown()
        t.dot(3, color)

    screen.update()

time.sleep(2)
turtle.done()
