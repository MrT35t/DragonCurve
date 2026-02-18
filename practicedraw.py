# import turtle, declare a turtle and a screen
import turtle
win = turtle.Screen()
donny = turtle.Turtle()
donny.shape('turtle')
donny.color('green')
donny.fillcolor('orange')

def square(side_length, color1):
    donny.color(color1)
    donny.begin_fill()
    donny.forward(side_length)
    donny.right(90)
    donny.forward(side_length)
    donny.right(90)
    donny.forward(side_length)
    donny.right(90)
    donny.forward(side_length)
    donny.right(90)
    donny.end_fill()

square(100, 'yellow')
donny.up()
donny.goto(-200, 200)
donny.down()
# circle can take up to 3 parameters. Radius, amount of circle, steps
donny.circle(50, 360, 10)
square(150, 'blue')
# close withdow when clicked.
win.exitonclick()


