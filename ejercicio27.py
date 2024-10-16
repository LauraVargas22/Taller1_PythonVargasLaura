''' 
Suma de número pares hasta que se introduce un impar
Mariana Vargas 
'''

print ("SUMA DE NÚMEROS PARES")
numUsuario = int(input("Ingrese el número que desea sumar: "))
suma = 0

while (numUsuario %2== 0):
  suma += numUsuario
  print (f"La suma de los números ingresados es {suma}") 

  numUsuario = int(input("Ingrese otro número: "))

print ("Se ha ingresa un número IMPAR")