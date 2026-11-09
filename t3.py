import random

a = float(input("Ingrese a: "))
b = float(input("Ingrese b: "))
c = float(input("Ingrese c: "))
d = float(input("Ingrese d: "))
cantidad = int(input("Ingrese la cantidad: "))
puntos_elipse = 0
puntos_interseccion = 0

for i in range(cantidad):
    x = random.uniform(-a, a)
    y = random.uniform(-b, b)
    
    formula_elipse = (x * x) / (a * a) + (y * y) / (b * b)
    formula_hiperbola = (x * x) / (c * c) - (y * y) / (d * d)
    
    if formula_elipse <= 1:
        puntos_elipse = puntos_elipse + 1
        
        if formula_hiperbola >= 1:
            puntos_interseccion = puntos_interseccion + 1

area_elipse = 3.14159 * a * b
area_interseccion = (puntos_interseccion / puntos_elipse) * area_elipse

print("Puntos en elipse:", puntos_elipse)
print("Puntos en interseccion:", puntos_interseccion)
print("Area elipse:", area_elipse)
print("Area interseccion:", area_interseccion)