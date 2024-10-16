''' 
Determinar entre tres números cual es mayor
Mariana Vargas 
'''
#Pedir al usuario que ingrese los tres números
num1 = int(input("Ingrese un número: "))
num2 = int(input("Ingrese un segundo número: "))
num3 = int(input("Ingrese un último número: "))
#Establecer las condiciones para evaluar cual es mayor
if (num1 > num2 and num1 > num3):
    print (f"El primer número ingresado {num1} es mayor")
elif (num2 > num1 and num2 > num3):
    print (f"El segundo número ingresado {num2} es mayor")
else:
    print (f"El tercer número ingresado {num3} es mayor")
    