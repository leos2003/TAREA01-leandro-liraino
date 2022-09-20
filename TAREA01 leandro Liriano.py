from __future__ import division
from ast import Num
from audioop import mul
Num1= int(input("ingrese el primer numero"))
Num2= int(input("ingrese el segundo numero"))
#aqui le agregamos los nombres a las operaciones y lo que queremos que hagan 
suma = Num1 + Num2

resta = Num1 - Num2

mult = Num1 * Num2

division = Num1 / Num2
# aqui le decimos a la maquina que usando los datos anteriores realize las operaciones 
print("la suma de %s y %s es %s" % (Num1, Num2, suma))

print("la resta de %s y %s es %s" % (Num1, Num2, resta))

print("la multiplicacion de %s y %s es %s" % (Num1, Num2, mult))

print("la division de %s y %s es %s" % (Num1, Num2, division))
