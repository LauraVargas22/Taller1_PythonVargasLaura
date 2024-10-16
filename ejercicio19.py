''' 
A continuación se convertirá una calificación numérica 
en base al sistema de calificación por letras.
Mariana Vargas 
'''
print ("CONVERSIÓN DE CALIFICACIÓN NUMÉRICA A LETRAS")
nota = int(input("Ingrese su calificación numérica 0 a 100: "))

match nota:
    case _ if (nota >=90 and nota <=100):
        print ("Su nota es A")
    case _ if (nota >= 80 and nota <=89):
        print ("Su nota es B")
    case _ if (nota >= 70 and nota <=79):
        print ("Su nota es C")
    case _ if (nota >= 60 and nota <=69):
        print ("Su nota es D")
    case _ if (nota >= 0 and nota <= 59):
        print ("Su nota es F")
    case _: 
        print ("Ha ocurrido un ERROR")
     
        
