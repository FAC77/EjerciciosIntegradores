#Para resolución de Ejercicio 1
#  1. Escribir una función que calcule el máximo común divisor entre dos números.


def divisores(numero):
    resultado = set()
    for i in range(1,numero + 1):
        if numero % i == 0:
            resultado.add(i)
    return resultado


def calcular_mcd(numero1, numero2):
    divisores_numero1 = divisores(numero1)
    divisores_numero2 = divisores(numero2)
    interseccion = divisores_numero1.intersection(divisores_numero2)
    resultado = 1
    for i in interseccion:
        if i > resultado:
            resultado = i
    return resultado


#Para resolución de Ejercicio 2
# 2. Escribir una función que calcule el mínimo común múltiplo entre dos números
def calcular_mcm(numero1, numero2):
    return((numero1 * numero2)/calcular_mcd(numero1, numero2))


print(calcular_mcd(150, 1100))

print(calcular_mcm(150, 1100))
