import turtle
import colorsys

screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Star Spiral Animation")

t = turtle.Turtle()
t.speed(0)
turtle.tracer(2)
t.hideturtle()

hue = 0.0

for i in range(300):
    color = colorsys.hsv_to_rgb(hue, 1, 1)
    t.pencolor(color)
    t.forward(i * 3)
    t.right(145)
    hue += 0.005

t.up()
t.goto(0, -320)
t.color("white")
t.write("PYTHONKING", align="center", font=("Arial", 20, "bold"))

turtle.done()
