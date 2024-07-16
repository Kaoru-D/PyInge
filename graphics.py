import matplotlib.pyplot as plt

Valores1 = [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
Valores2 = [5, 4, 3, 2, 1, 0, 1, 2, 3, 4, 5]

plt.plot(Valores1, label="Dato 1")
plt.plot(Valores2, label="Dato 2")
plt.legend(loc="lower right")
plt.style.use("ggplot")
plt.title("Datos A Evaluar")

x = [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
y = 1
fx = []
for i in x:
    fx.append(i ** 2 + y)

print(f"F(x) = {fx}")
plt.plot(x, fx)


def importarArchivos(ruta):
    with open(ruta) as archivo:
    contenido = [int(fila) for fila in open(ruta).readlines()]
    archivo.close()
    return contenido
sensor = importarArchivos("sensor.txt")
plt.plot(sensor)


plt.style.use("dark_background")
plt.title("Datos A Evaluar")
