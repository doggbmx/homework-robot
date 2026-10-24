# Ventosa: mover un cubo (herramienta: ventosa)
import robot
import time

# Ejemplo oficial de Huenit: llevar el cubo rojo a la zona A
# Ruta: A -> B -> A -> C -> D -> C

robot.moveG0(-163, 245, 50)    # A: encima del cubo
robot.moveG0(-163, 245, -35)   # B: tocar la cara de arriba
robot.suctionOn()
time.sleep(1)

robot.moveG0(-163, 245, 50)    # A: subir con el cubo
robot.moveG0(120, 250, 50)     # C: encima de la zona A
robot.moveG0(120, 250, -35)    # D: bajar
robot.suctionOff()
time.sleep(1)

robot.moveG0(120, 250, 50)     # C: subir
