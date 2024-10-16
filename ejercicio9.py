''' 
Clasificar a una persona según su edad
Mariana Vargas 
'''
edad = int (input("Ingrese su edad: "))

if (edad >= 0 and edad <12):
    print ("La edad corresponde a un NIÑO")
elif (edad >= 13 and edad <17):
    print ("La edad ingresada corresponde a un ADOLESCENTE")
elif (edad >=18 and edad < 64):
    print ("La edad ingresada corresponde a un ADULTO") 
else:
    print ("La edad ingresada corresponde a un ANCIANO")
