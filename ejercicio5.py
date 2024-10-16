''' 
Imprimir un día de la semana de acuerdo al número escogido
Mariana Vargas 
'''

numero = int (input(f"Ingrese un número del 1 al 7: "))

match numero:
    case 1:
        print ("El día correspondiente es Lunes")
    case 2:
        print ("El día correspondiente es Martes")
    case 3:
        print ("El día correspondiente es Miércoles")
    case 4:
        print ("El día correspondiente es Jueves")
    case 5:
        print ("El día correspondiente es Viernes")
    case 6:
        print ("El día correspondiente es Sábado")
    case 7:
        print ("El día correspondiente es Domingo")
    case _: 
        print ("Número inválido")