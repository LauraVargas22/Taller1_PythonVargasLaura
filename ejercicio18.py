''' 
Se evaluará el sistema de créditos universitarios teniendo en
cuenta materias cursadas y puntaje obtenido de cada una.
Mariana Vargas 
'''

print ("SISTEMA DE EVALUACIÓN CRÉDITOS UNIVERSITARIOS")
materiasCursadas = int (input("Ingrese el número de materias que ha cursado: "))
#Definir variables
puntajeMin = 60
CreditosPorMaterias = 3
CreditosTotales = 0

#De acuerdo con el número de materias se pide el puntaje
for m in range (materiasCursadas):
    puntaje = float (input(f"Ingrese el puntaje de la materia {m +1}: "))
#Definimos si se aprobó o reprobó la materia teniendo en cuenta el puntaje
    if (puntaje >= puntajeMin):
        print (f"La materia {m +1} ha si APROBADA")
    #Suma de los créditos por cada materia aprobada
        CreditosTotales += CreditosPorMaterias 
    else: 
        print (f"La materia {m + 1} ha sido REPROBADA")
  
print (f"El número total de créditos obtenidos por materia es: {CreditosTotales}")