from turtle import Turtle


class Raqueta(Turtle):
    def __init__(self, x, y, width, height):
        super().__init__()
        self.color("white")
        self.shape("square")
        self.penup()
        self.setheading(90)
        self.shapesize(width / 20, height / 20, 1)
        self.goto(x, y)

    def mover_arriba(self):
        self.forward(20)
        # print("arriba")

    def mover_abajo(self):
        self.backward(20)
        # print("abajo")

        # Se puede hacer tambien de esta manera
        # new_y = self.ycor() - 20
        # self.goto(self.xcor(), new_y)
