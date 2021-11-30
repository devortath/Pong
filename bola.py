from turtle import Turtle


class Bola(Turtle):
    def __init__(self):
        super().__init__()
        self.color("yellow")
        self.shape("circle")
        self.penup()
        self.shapesize(1, 1, 1)
        self.goto(0, 0)
        self.direccion_x = 10
        self.direccion_y = 10
        self.velocidad = 0.08

    def rebotar_y(self):
        self.direccion_y *= -1

    def rebotar_x(self):
        self.direccion_x *= -1

        # Manera facil de aumentar velocidad
        self.velocidad *= 0.9

    def mover(self):
        nueva_x = self.xcor() + self.direccion_x
        nueva_y = self.ycor() + self.direccion_y
        self.goto(nueva_x, nueva_y)

    def resetear(self):
        """Resetea la bola a su lugar inicial y sale en direccion contraria a por donde salió"""
        self.rebotar_x()
        self.rebotar_y()

        #Reseteamos velocidad
        self.velocidad = 0.08

        # Se puede hacer de esta manera, pero es mas elegante y facil hacerlo con la propieda time del update
        # if self.direccion_x > 0:
        #     self.direccion_x = 10
        # else:
        #     self.direccion_x = -10

        # if self.direccion_y > 0:
        #     self.direccion_y = 10
        # else:
        #     self.direccion_y = -10

        self.goto(0, 0)
