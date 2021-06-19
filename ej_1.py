################
# Camila Sol Ampuero - @CamilaSol
# plantilla de ejercicio
# UNRN Andina - Introducción a la Ingenieria en Computación
################

# 1. Pares e impares

def par_o_impar(numero):
    cadena = str(numero)
    lista = list( map( int, cadena))
    print(lista)
    ultimo_numero = lista[-1]
    
    if ultimo_numero == 0 or ultimo_numero == 2 or ultimo_numero == 4 or ultimo_numero == 6 or ultimo_numero == 8:
        return True
    else:
        return False
    
def prueba():
    while True:
        numero_a_identificar = int( input( "ingrese numero para verificar"))
        resultado = par_o_impar(numero_a_identificar)
        print(resultado)
    
if __name__ == "__main__":
    prueba()
