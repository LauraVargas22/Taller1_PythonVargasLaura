''' 
Se calculará el factorial del número ingresado por el usuario.
Mariana Vargas 
'''
import math
#Solicitar número
print ("FACTORIAL DE UN NÚMERO")
num = int(input("Ingrese un número"))

factorial = 1

for i in range(1,num +1):
    factorial *= i
print (f"El factorial del número {num} es: {factorial}")
