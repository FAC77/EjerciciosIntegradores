# 3. Escribir un programa que reciba una cadena de caracteres y devuelva un diccionario con
# cada palabra que contiene y la cantidad de veces que aparece (frecuencia)


def poblar_dic(lista_palabras):
    resultado = dict()
    for palabra in lista_palabras:
        if (palabra not in resultado):
            resultado[palabra] = 1
        else:
            resultado[palabra] = resultado[palabra] + 1
    return resultado

frase = input("Ingrese la frase a analizar: ")
#Separamos lfrase en sus palabras.
lista_internedia= frase.split()

print(poblar_dic(lista_internedia))






# def poblar_dic(frase):
#     palabra = ''
#     for letra in frase:
#         print(letra)
#         if letra != ' ':
#             palabra = palabra + letra
#         else:
#             resultado
