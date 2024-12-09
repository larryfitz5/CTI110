import turtle

# Setup screen and turtle
screen = turtle.Screen()
t = turtle.Turtle()

# Draw a square using a loop
for _ in range(4):
    t.forward(100)
    t.left(90)

# Move turtle to a new location to draw a triangle
t.penup()
t.goto(-50, -50)
t.pendown()

# Draw a triangle using a loop
for _ in range(3):
    t.forward(100)
    t.left(120)

# End program
screen.mainloop()
