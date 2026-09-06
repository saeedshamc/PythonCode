import turtle

p = turtle.Turtle()
s = turtle.Screen()
s.bgcolor("black")
p.pencolor('#7c909c')   # lowercase hex
p.speed(10)
colors = ('#9c3758', '#df8752', '#1a266b', '#156a14')

for n in range(5):
    p.pencolor(colors[n % 4])
    for x in range(8):
        p.pensize(2)
        for i in range(2):
            p.circle(80 + n * 20, 90)
            p.left(90)
        p.left(45)

p.hideturtle()
s.mainloop()    # safer than exitonclick
