''' 
Adivinar el número usando While
Mariana Vargas 
'''
print ("Intenta adivinar el número")
import random
num_secreto = random.randint(1,100)
numeroUsuario = int (input("Ingrese un número del 1 al 100: "))

while (numeroUsuario != num_secreto):
    if (numeroUsuario > num_secreto):
            print ("El número ingresado es MAYOR")
    elif (numeroUsuario < num_secreto):
            print ("El número ingresado es MENOR")

    numeroUsuario = int (input("Intenta nuevamente"))

print ("Has adivinado el número, ¡Felicidades!")

