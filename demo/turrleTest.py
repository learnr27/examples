import turtle
turtle.setup(800, 800)
# turtle.backward(200)
# turtle.fd(100)

# turtle.right(45)
# turtle.fd(100)

# turtle.setheading(120)
# turtle.fd(100)

# turtle.goto(20,50)

# turtle.circle(100,360)
# turtle.undo()
# turtle.speed(100)

# for i in range(6):
#     turtle.seth(i * 60)
#     turtle.fd(100)

# turtle.penup()
# turtle.fd(0)

turtle.begin_fill()

turtle.pendown()
turtle.pensize(5)
turtle.color('red')
turtle.circle(200,360)

turtle.end_fill()
turtle.clear()

turtle.fd(10)

turtle.reset()


turtle.screensize(1000,1000)
turtle.hideturtle()
turtle.done()