# Pinza: mover un cubo (herramienta: pinza)
import robot
import time

# Ejemplo oficial de Huenit con la pinza blanda
piso = -20          # Z de la mesa con la pinza puesta
alto_cubo = 25      # el cubo mide 25 mm

robot.moveG0(-150, 150, 70)
robot.gripper(1)                                # abrir
time.sleep(2)
robot.moveG0(-150, 150, piso + alto_cubo - 10)  # 10 mm bajo la cara de arriba
robot.gripper(2)                                # agarrar
time.sleep(2)

robot.moveG0(-150, 150, 70)
robot.moveG0(150, 150, 70)                      # encima de la zona B
robot.moveG0(150, 150, piso + alto_cubo - 10)
robot.gripper(1)                                # soltar
time.sleep(2)

robot.moveG0(150, 150, 70)
robot.gripper(0)                                # reposo
