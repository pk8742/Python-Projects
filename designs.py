import turtle


triangle = turtle.Turtle()
triangle.penup()
triangle.goto(-230,200)
triangle.pendown()
for i in range(3):
    triangle.backward(50)
    triangle.right(120)


square = turtle.Turtle()
square.penup()
square.goto(-200,200)
square.pendown()
for i in range(4):
    square.forward(50)
    square.left(90)

pent = turtle.Turtle()
pent.penup()
pent.goto(-120,200)
pent.pendown()
pent.left(90)
pent.forward(50)
pent.right(60)
pent.forward(50)
pent.right(60)
pent.forward(50)
pent.right(60)
pent.forward(50)
pent.right(90)
pent.forward(87)
pent.right(180)




turtle.done()
