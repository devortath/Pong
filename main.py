from turtle import Screen
from raqueta import Raqueta
from bola import Bola
from puntuaciones import Puntuaciones
import time

pantalla = Screen()
pantalla.setup(800, 600)
pantalla.bgcolor("black")
pantalla.title("Pong")
pantalla.tracer(0)

puntuaciones = Puntuaciones()

raqueta1 = Raqueta(-350, 0, 20, 100)
raqueta2 = Raqueta(350, 0, 20, 100)
pelota = Bola()
pantalla.listen()

# Control J1
pantalla.onkeypress(raqueta1.mover_arriba, "w")
pantalla.onkeypress(raqueta1.mover_abajo, "s")
# Control J2
pantalla.onkeypress(raqueta2.mover_arriba, "Up")
pantalla.onkeypress(raqueta2.mover_abajo, "Down")

jugar = True

while jugar:
    time.sleep(pelota.velocidad)
    pantalla.update()
    pelota.mover()

    # Si hay colision con el techo o el suelo, rebota
    if pelota.ycor() >= 280 or pelota.ycor() <= -280:
        pelota.rebotar_y()

    # Detectar colisiones con raquetas
    if (
        pelota.distance(raqueta2) < 50
        and pelota.xcor() > 320
        or pelota.distance(raqueta1) < 50
        and pelota.xcor() < -320
    ):
        pelota.rebotar_x()

    # Pelota se escapa por la derecha
    if pelota.xcor() > 380:
        pelota.resetear()
        puntuaciones.incrementar_puntuacion_j1()

    # Pelota se escapa por la izquierda
    if pelota.xcor() < -380:
        pelota.resetear()
        puntuaciones.incrementar_puntuacion_j2()


pantalla.exitonclick()
