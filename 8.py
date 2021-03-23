import turtle
import time

p = turtle.Pen()
p.shape("turtle")

for n in range(3, 9):
    p.setheading(0)
    p.penup()
    p.goto(0 + (n - 2) * 10, 0)
    p.pendown()
    t = ((n - 2) * 180) / n
    p.left(180 - (t / 2))
    p.forward(200)

    for i in range(n-1):
        # print(n)
        t = ((n - 2) * 180) / n
        p.left(180 - t)
        p.forward(200)


time.sleep(5)