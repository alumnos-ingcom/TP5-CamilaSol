################
# Camila Sol Ampuero - @CamilaSol
# plantilla de ejercicio
# UNRN Andina - Introducción a la Ingenieria en Computación
################

# 3.Tribonacci

def trib(numero):
    serie = [1,1,1]
    for i in range(numero -3):
        serie.append(serie[-1] + serie[-2] + serie[-3])
     
    n_esimo = serie[numero -1]                                 
    return n_esimo


def prueba():
    numero = input('Ingrese un numero entero positivo: ')
    numero = int(numero)
    print(trib(numero))
    

if __name__ == "__main__":
    prueba()
