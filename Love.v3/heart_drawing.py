import turtle as t, math as m, random as r, time

s = t.Screen()
s.bgcolor("black")
s.tracer(0)
t.hideturtle()

for i in range(320):
    a = 2 * m.pi * i / 320
    xo = 16 * (m.sin(a) ** 3) * 16
    yo = (13 * m.cos(a) - 5 * m.cos(2 * a) - 2 * m.cos(3 * a) - m.cos(4 * a)) * 16
    L = r.uniform(0.15, 0.5)
    xi, yi = xo * (1 - L), yo * (1 - L)

    for j in range(10):
        f = j / 10
        t.pencolor(1 - 0.6 * f, 0.7 * (1 - f), 0.8 * (1 - f))
        t.width(2)
        t.penup()
        t.goto(xo + (xi - xo) * f, yo + (yi - yo) * f)
        t.pendown()
        t.goto(xo + (xi - xo) * (f + 0.1), yo + (yi - yo) * (f + 0.1))
    s.update()
    time.sleep(0.02)

t.done()
