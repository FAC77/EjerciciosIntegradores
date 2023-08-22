# 5. Sabiendo que ValueError es la excepción que se lanza cuando no podemos convertir una
# cadena de texto en su valor numérico, escriba una función get_int() que lea un valor entero
# del usuario y lo devuelva, iterando mientras el valor no sea correcto. Intente resolver el
# ejercicio tanto de manera iterativa como recursiva.

#Version iterativa
def get_int():
    while True:
        texto = input("Ingrese un numero: ")
        try:
            numero = float(texto)
            return numero
        except ValueError:
            print("El valor ingresado es inválido, ingrese un nuevo valor.")


#Version recursiva.
def get_int_rec():
    texto = input("Ingrese un numero: ")
    try:
        numero = float(texto)
        return numero
    except ValueError:
        print("El valor ingresado es inválido.")
        return get_int_rec()

print(get_int())
print("ahora se pone fulero!")
print(get_int_rec())



