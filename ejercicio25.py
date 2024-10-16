''' 
Mostrar al usuario los número pares en un rango establecido
Mariana Vargas 
'''
print ("Número pares en un rango")
#Solictar el rango al usuario
num1 = int (input("Ingrese un número como valor de inicio al rango"))
num2 = int (input("Ingrese un número como valor final del rango"))

print (f"Los números pares en el rango de {num1} a {num2} son:")
for n in range (num1, num2+1):
        if n % 2 == 0:
            print (n)



