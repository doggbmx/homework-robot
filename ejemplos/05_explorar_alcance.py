# Explorar el alcance (herramienta: ventosa)
import robot

# checkXYZ(x, y, z) devuelve 1 si el brazo puede llegar y 0 si no
for z in [0, 50, 100, 150]:
    fila = ""
    for y in range(100, 351, 50):
        if robot.checkXYZ(0, y, z):
            fila = fila + " si "
        else:
            fila = fila + " -- "
    print("Z =", z, " Y de 100 a 350:", fila)

# Prueba: ¿qué pasa si pedimos un punto imposible?
robot.moveG0(0, 180, 150)
