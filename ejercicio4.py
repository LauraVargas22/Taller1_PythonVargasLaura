''' 
Definir a que clasificación de triángulos pertenece según sus lados
Mariana Vargas 
'''
#Ingreso de la longitud de los lados del triángulo
lado1 = float (input(f"Ingrese la longitud de uno de los lados del triángulo: "))
lado2 = float (input(f"Ingrese la longitud del segundo lado del triángulo: "))
lado3 = float (input(f"Ingrese la longitud del tercer lado del triángulo: "))

#Clasificación del triángulo según sus lados
if (lado1 == lado2 == lado3):
    print ("La longitud de los lados corresponden a un triángolo EQUILÁTERO")
elif (lado1 != lado2 != lado3 ):
    print ("La longitud de los lados corresponden a un triángolo ESCALENO")
else: 
    print ("La longitud de los lados corresponden a un triángolo ISÓSCELES")