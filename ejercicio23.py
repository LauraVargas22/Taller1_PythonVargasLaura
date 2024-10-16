''' 
Se contará la cantidad de vocales que hay en 
una cadena de texto.
Mariana Vargas 
'''
print ("CONTADOR DE VOCALES")
mensaje = str(input("Ingrese la cadena de texto: "))
vocales = 'aeiou'
totalvocales = 0

for i in mensaje:
    if i in vocales:
        totalvocales += 1
print (f"El mensaje {mensaje} contiene {totalvocales} de vocales ")
