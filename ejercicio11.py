''' 
Conversión de temperaturas de Celsius a Fahrenheit y viceversa
Mariana Vargas 
'''
import os 
isActive =True
#Se pedira el número correspondiente a la temperatura
temperatura = float (input("Ingrese la temperatura que desea convertir: "))
# Se declaran las opciones de los valores de la temperatura
opcionestem = 'c.celsius\nf.fahrenheit\n0.Salir'
opcionusuario = ''

os.system ('cls')
#Se muestra al usuario las opciones
print (opcionestem)
opcionusuario = input ('Seleccione el tipo de temperatura ingresado:_')
#De acuerdo a la selección se realiza la conversión
match opcionusuario:
    case 'c.celsius':
        fahrentheit = float((temperatura *1.8)+32)
        print (f"La temperatura {temperatura} en fahrenheit equivale a: {fahrentheit}")
    case 'f.fahrenheit':
        celsius = float((temperatura-32)/1.8)
        print (f"La temperatura {temperatura} en celsius equivale a: {celsius}")
    case 0:
      isActive = False
    case _:
        print ('Ha ocurrido un error en la selección')