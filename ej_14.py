################
# Camila Sol Ampuero - @CamilaSol
# plantilla de ejercicio
# UNRN Andina - Introducción a la Ingenieria en Computación
################

# 14. Números capicúa

def capicua(numero):
    return str(numero) == str(numero)[::-1]
        
   

def prueba():
    numero = input('Ingrese un numero para saber si es capicua: ')
    numero = int(numero)
    resultado = capicua(numero)
    
    if resultado == True:
        print('Es capicua')
    else:
        print('No es capicua')

             
if __name__ == "__main__":
    prueba()
