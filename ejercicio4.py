# 4. Escribir una función que reciba una cadena de caracteres y devuelva un diccionario con cada
# palabra que contiene y la cantidad de veces que aparece (frecuencia). Escribir otra función
# que reciba el diccionario generado con la función anterior y devuelva una tupla con la
# palabra más repetida y su frecuencia.

def poblar_dic(lista_palabras):
    resultado = dict()
    for palabra in lista_palabras:
        if (palabra not in resultado):
            resultado[palabra] = 1
        else:
            resultado[palabra] = resultado[palabra] + 1
    return resultado


def generar_tupla(dict_palabras):
    max = 0
    for clave in dict_palabras:
        if dict_palabras[clave] > max:
            max = dict_palabras[clave]
            clave_max = clave
    return (clave_max, dict_palabras[clave_max])

frase = input("Ingrese la frase a analizar: ")

#Separamos lfrase en sus palabras.
lista_internedia = frase.split()

#Generamos el diccionaro con la palabras como clave y la cantidad de repeticiones cono dato.
diccionario_resultado = poblar_dic(lista_internedia)

#Generamos una tupla conteniendo la palaba con mayoresrepeticiones.
tupla_resultado = generar_tupla(diccionario_resultado)

print(tupla_resultado)
