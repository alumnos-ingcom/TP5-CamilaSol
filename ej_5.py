################
# Camila Sol Ampuero - @CamilaSol
# plantilla de ejercicio
# UNRN Andina - Introducción a la Ingenieria en Computación
################

# 5. Inversión de mayusculas

def cambiar(texto):
    for caracter in texto:
        letra_mayus = caracter.isupper()
        letra_minus = caracter.islower()
        
        if letra_mayus == True:
            letra = caracter
            letra = letra.lower()
            texto = texto.replace(f"{caracter}", f"{letra}")
            
        elif letra_minus == True:
            letra = caracter
            letra = letra.upper()
            texto = texto.replace(f"{caracter}", f"{letra}")
        else:
            continue
        
    return texto
    
    
def prueba():
    texto = input('Ingrese un texto para cambiar sus mayusculas a minusculas y viceversa: ')
    print(cambiar(texto))
    
    
if __name__ == "__main__":
    prueba()
