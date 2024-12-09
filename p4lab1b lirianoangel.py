import turtle

# Setup screen and turtle
screen = turtle.Screen()
t = turtle.Turtle()

# Set pen color and size
t.pencolor("blue")
t.pensize(5)

# Draw first initial (e.g., "A")
t.left(75)
t.forward(100)
t.right(150)
t.forward(100)
t.backward(50)
t.right(105)
t.forward(25)

# Move to a new location for the second initial
t.penup()
t.goto(50, 0)
t.pendown()

# Draw second initial (e.g., "L")
t.left(90)
t.forward(100)
t.right(90)
for _ in range(2):
    t.circle(-25, 180)

# End program
screen.mainloop()
