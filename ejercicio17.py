''' 
Por medio de este programa se calculará la calificación
final teniendi en cuenta tareas extras
Mariana Vargas 
'''

print ("A continuación se evaluará su calificación final")
calificación = int (input("Ingrese su calificación: "))
tareas_ad = input ('¿Realizo tareas adivionales?, elija (Si o No)')
if (tareas_ad == 'Si'):
    valortareas_ad = (calificación * 5)/100
    caliFinal = calificación + valortareas_ad
    if (caliFinal > 100):
        print ("Su calificación final es de 100")
    else:
        print (f"Su calificación final es de: {caliFinal}")
else:
    print (f"Su calificación final es de {calificación}")
