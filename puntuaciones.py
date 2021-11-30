from turtle import Turtle

ALINEACION = "center"
FUENTE = ("Courier", 50, "normal")


class Puntuaciones(Turtle):
    def __init__(self):
        super().__init__()
        self.score_j1 = 0
        self.score_j2 = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.actualizar_puntuacion()

    def actualizar_puntuacion(self):
        self.goto(-100, 200)
        self.write(self.score_j1, align=ALINEACION, font=FUENTE)
        self.goto(100, 200)
        self.write(self.score_j2, align=ALINEACION, font=FUENTE)

    def incrementar_puntuacion_j1(self):
        self.score_j1 += 1
        self.clear()
        self.actualizar_puntuacion()

    def incrementar_puntuacion_j2(self):
        self.score_j2 += 1
        self.clear()
        self.actualizar_puntuacion()

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", align=ALINEACION, font=FUENTE)
