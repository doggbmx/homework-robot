# Saludo (asentir 3 veces) (herramienta: ventosa)
import robot
import time

# El brazo saluda moviendo la "cabeza" arriba y abajo
robot.goHome()

for i in range(3):
    robot.moveG0(0, 200, 80)   # arriba
    robot.moveG0(0, 200, 20)   # abajo
    print("Saludo", i + 1)

robot.goHome()
print("¡Hola!")
