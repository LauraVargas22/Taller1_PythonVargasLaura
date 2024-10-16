''' 
A partir de un número aleatorio generado por el programa establecer si el número
ingresado es mayor, menor o igual al generado.
Mariana Vargas 
'''
import random
num_aleatorio = random.randint (1,10)

num_usuario = int (input(f"Intenté adivinar el número del 1 al 10: "))

if (num_usuario > num_aleatorio):
    print ("El número ingresado es mayor")
elif (num_usuario < num_aleatorio):
    print ("El número ingresado es menor")
else:
    print ("Has adivinado el número, felicidades")