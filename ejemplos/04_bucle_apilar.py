# Bucle: apilar dos cubos (herramienta: ventosa)
import robot
import time

MESA = -60     # Z de la mesa con la ventosa
CUBO = 25      # tamaño del cubo en mm
SEGURO = 50    # altura para viajar sin chocar

cubos = [(-163, 245), (40, 300)]   # rojo y amarillo
destino = (120, 250)               # zona A

robot.goHome()
for i in range(len(cubos)):
    x, y = cubos[i]
    robot.moveG0(x, y, SEGURO)
    robot.moveG0(x, y, MESA + CUBO)        # tocar la cara de arriba
    robot.suctionOn()
    time.sleep(1)
    robot.moveG0(x, y, SEGURO)

    altura = MESA + CUBO * (i + 1)         # cada cubo va 25 mm más arriba
    robot.moveG0(destino[0], destino[1], SEGURO)
    robot.moveG0(destino[0], destino[1], altura)
    robot.suctionOff()
    time.sleep(1)
    robot.moveG0(destino[0], destino[1], SEGURO)
    print("Cubo", i + 1, "apilado a Z =", altura)

robot.goHome()
