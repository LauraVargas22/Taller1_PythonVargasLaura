''' 
Clasificar una nota teniendo en cuenta algunas características
Mariana Vargas 
'''
nota = int (input("Ingrese la nota correspondiente: "))

if (nota >= 90 and nota <=100):
    print ("Su nota es A")
elif (nota >=80 and nota <=89):
    print ("Su nota es B")
elif (nota >=70 and nota <= 79):
    print ("Su nota es C")
elif (nota >=60 and nota <= 69):
    print ("Su nota es D")
else:
    print ("Su nota es F")