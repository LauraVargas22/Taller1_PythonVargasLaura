''' 
Se desarrollorá un juego de adivinanza de letras
Mariana Vargas 
'''
#Definimos la letra secreta a adivinar
letra_secreta = 'm'

letraSeleccionada = str(input("Intenté adivinar la letra secreta, ingrese su selección: "))

match letraSeleccionada:
    case 'm':
        print ("Has adivinado la letra 🤩")
    case _:
        print ("La letra no fue adivinada ☹️")


