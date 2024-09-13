import turtle

wn = turtle.Screen()
turtle.screensize(800,800)

painter = turtle.Turtle()
painter.speed(0)
n = 5
for i in range(n):
    stop = False
    while not stop:
        painter.penup()
        painter.forward(1)
        print(str(painter.distance(0,0)))
        if painter.distance(0,0) >= 200:
            stop = True
    painter.stamp()
    painter.goto(0,0)
    painter.left(360/n)

wn.mainloop()
