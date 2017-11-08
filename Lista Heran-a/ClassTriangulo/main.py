from ClassTriangulo import *


print(" Calculo do triangulo ")
a = input("insira o 1º lado")
b = input("insira o 2º lado")
c = input("insira o 3º lado")

triangulo = Triangulo(a,b,c)

print(triangulo.perimetro())
print(triangulo.getMaior())
