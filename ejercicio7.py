''' 
Determinar si un número es positivo o negativo
Mariana Vargas 
'''
num = int (input(f"Ingrese un número: "))

#Establecer condiciones para determinar si es positivo, negativo o cero.
if (num > 0):
    print ("El número ingresado es POSITIVO")
elif (num < 0):
    print ("El número ingresado es NEGATIVO")
else:
    print ("El número ingresado es CERO")