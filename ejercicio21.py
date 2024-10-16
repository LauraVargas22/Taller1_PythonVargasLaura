''' 
Se clasificará un triángulo según a sus ángulos
Mariana Vargas 
'''
print ("CLASIFICACIÓN DE UN TRIÁNGULO SEGÚN SUS ÁNGULOS")
angulo1 = float (input("Ingrese un ángulo del triángulo: "))
angulo2= float (input("Ingrese otro ángulo del triángulo: "))
angulo3 = float (input("Ingrese el último ángulo del triángulo: "))

if (angulo1 <90 and angulo2 <90 and angulo3 <90):
    print ("El triángulo es AGUDO")
elif (angulo1 >90  or angulo2 >90 or angulo3 > 90):
    print ("El triángulo es OBTUSO")
else:
    print ("El triángulo es RECTÁNGULO")
