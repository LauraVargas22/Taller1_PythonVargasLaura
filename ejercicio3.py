''' 
Calculadora de operaciones básicas con dos números
Mariana Vargas 
'''
import os

isActive = True
#Declarar as opciones que se van a tener en la calculadora
opcionescalculadora = '+.Suma\n-.Resta\n*.Multiplicación\n/.División\n0.Salir'
opcionUsuario = ''

#Ingreso de los números los cuales van a intervenir en las operaciones
numero1 = float (input(f"Ingrese un número: "))
numero2 = float (input(f"Ingrese otro número: "))

#Permitir la elección de la operación a realizar
while (isActive):
    os.system('cls')
    print (opcionescalculadora)
    opcionUsuario = input('Seleccione:_')

#Declaración de cada uno de los casos teniendo en cuenta las operaciones a seleccionar
    match opcionUsuario:
        case '+':
            suma = numero1 + numero2
            print (f"La suma de los números ingresados es: {suma}")
        case '-':
            resta = numero1 - numero2
            print (f"La resta de los número ingresados es: {resta}")
        case '*':
            multiplicación = numero1 *numero2
            print (f"La multiplicación de los números ingresados es: {multiplicación}")
        case '/':
            división = numero1 / numero2
            print (f"La división de los números ingresados es: {división}")
        case '0':
            isActive = False
        case _:
            print ('Error en la opción seleccionada')
            os.system('pause')