''' 
Suma de los número anteriores a n
Mariana Vargas 
'''
#Solicitar n al usuario
num = int(input("Ingrese un número entero positivo: "))
suma = 0

if (num < 0):
    print ("ERROR")
else: 
    for i in range (1, num + 1):
        suma += i
    print (f"La suma de los primero {num} enteros es {suma}")
        
