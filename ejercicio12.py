''' 
Determinar el Indice de Masa Corporal de acuerdo a los datos ingresados
por el usuario (peso en kg y altura en mt)
Mariana Vargas 
'''
print ("Evaluar Indice de Masa Muscular")
#Pedir al usuario el ingreso del peso y la altura
peso = float (input("Ingrese su peso en kilogramos: "))
altura = float (input("Ingrese su altura en metros: "))

#Declarar formula para determinar IMC
imc = float (peso/altura**2)

#Definir condiciones de acuerdo al resultado del IMC
if (imc < 18.5):
    print ("Su IMC corresponde a BAJO PESO")
elif (imc > 18.5 and imc <=24.9):
    print ("Su IMC corresponde a peso NORMAL")
elif (imc > 25 and imc <=29.9):
    print ("Su IMC corresponde a SOBREPESO")
else:
    print ("Su IMC corresponde a OBESIDAD")
