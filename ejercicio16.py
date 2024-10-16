''' 
Por medio de este programa se calculará el tiempo de
llegada de un automóvil en llegar a su destino
Mariana Vargas 
'''
#Solicitar al usuario velocidad y distancia
print ("Calculará su tiempo de viajes")
distancia = float (input("Ingrese la distancia en km a recorrer: "))
velocidad = float (input('Ingresa la velocidad promedio del automóvil en km/h: '))
#Definir formulas de tiempo
tiempoh = distancia / velocidad
tiempom = tiempoh * 60
#Mostrar al usuario el tiempo gastado
if (velocidad > 120):
    print ("Recuerde disminuir la velocidad")
    print (f"El tiempo que gastará en llegar a su destino serán {tiempoh} horas, lo que es igual a {tiempom}minutos")
else:
    print (f"El tiempo que gastará en llegar a su destino serán {tiempoh} horas, lo que es igual a {tiempom}minutos")
    