''' 
Se desarrollará un sistema de tarifas progresivas en un parqueadero
Mariana Vargas 
'''
print ("COSTO DEL PARQUEADERO")
numHoras = int (input("Ingrese el número de horas que estuvo en el parqueadero: "))

if (numHoras ==1):
    print ("El valor de estacionamiento es de $5")
elif (numHoras >1 and numHoras <=4):
    #Formula si las horas de parqueo son de 2 a 4
    costoTotal = 5 + (numHoras - 1)*4
    print (f"El costo total de estacionamiento es de ${costoTotal}")
else:
    #Formula si las horas de parque son mayores a 4
    costoTotal = 5 + 3*4 + (numHoras - 4)*3
    print (f"El costo total de estaciionamiento es de ${costoTotal}")
    