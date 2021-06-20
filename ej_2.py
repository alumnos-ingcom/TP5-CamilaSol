################
# Camila Sol Ampuero - @CamilaSol
# plantilla de ejercicio
# UNRN Andina - Introducción a la Ingenieria en Computación
################

# 2.Fibonacci

def fib(n):
    a = 2
    b = 1
    while a < n:
        print(a, end='   ' )
        a, b = b, a+b

def prueba():
    print()
fib(1000)

if __name__ == "__main__":
    prueba()
