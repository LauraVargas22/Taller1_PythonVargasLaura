''' 
Por medio de este programa se calculará el salario neto 
teniendo en cuenta el impuesto que recibe cada persona de acuerdo al país correspondiente.
Mariana Vargas 
'''
import os 
#Se pedirá al usuario su salario bruto y su país de residencia
print ("Pronto se calculará su salario neto")
salario_bruto = int(input("Ingrese su salario bruto: "))
opciones_pais = 'pais A\n pais B\npais C\nNo aplica'
opcion_seleccionada = ''
os.system ('cls')
print (opciones_pais)
opcion_seleccionada = input('Seleccione:_')

#Definir salario neto teniendo en cuenta la opción seleccionada por el usuario
match opcion_seleccionada:
    case 'pais A':
        impuesto = (salario_bruto*20)/100
        salario_neto = salario_bruto - impuesto
        print (f'Su salario neto es de {salario_neto} se le ha aplicado un impuesto del 20% que corresponde a {impuesto}')
    case 'pais B':
        impuesto = (salario_bruto*15)/100
        salario_neto = salario_bruto - impuesto
        print (f'Su salario neto es de {salario_neto} se le ha aplicado un impuesto del 15% que corresponde a {impuesto}')
    case 'pais C':
        impuesto = (salario_bruto*10)/100
        salario_neto = salario_bruto - impuesto
        print (f'Su salario neto es de {salario_neto} se le ha aplicado un impuesto del 10% que corresponde a {impuesto}')
    case 'No aplica':
        impuesto = (salario_bruto*25)/100
        salario_neto = salario_bruto - impuesto
        print (f'Su salario neto es de {salario_neto} se le ha aplicado un impuesto del 25% que corresponde a {impuesto}')
    case _:
        print ("Ha ocurrido un error vuelva a intentarlo")