''' 
Determinar si el año ingresado es bisiesto
Mariana Vargas 
'''
año = int (input(f"Ingrese un año: "))

if (año %4 == 0) and (año %100 !=0 or año %400 ==0):
    print ("El año ingresado es BISIESTO")
else:
    print ("El año ingresado no es bisiesto")    