def CalculoAreaTriangulo(base, altura):
    area = 0.5 * base * altura
    print('El área de su triángulo es', area)

print('Vamos a hallar el área de un triángulo')
base = float(input('Ingrese la base '))
altura = float(input('Ingrese la altura '))
CalculoAreaTriangulo(base, altura)