# 6. Crear una clase llamada Persona. Sus atributos son: nombre, edad y DNI. Construya los
# siguientes métodos para la clase:
#   * Un constructor, donde los datos pueden estar vacíos.
#   * Los setters y getters para cada uno de los atributos. Hay que validar las entradas de
#       datos.
#   * mostrar(): Muestra los datos de la persona.
#   * Es_mayor_de_edad(): Devuelve un valor lógico indicando si es mayor de edad.


class Persona():

    def __init__(self, nombre='Juan Perez', edad=33, dni=1):
        # self.__nombre = nombre
        self.nombre = nombre
        self.edad = edad
        self.DNI = dni

    @property
    def nombre(self):
        return self.__nombre

    @property
    def edad(self):
        return self.__edad

    @property
    def DNI(self):
        return self.__dni

    @nombre.setter
    def nombre(self, nuevo_nombre):
        if (nuevo_nombre > '' and len(nuevo_nombre) > 1):
            self.__nombre = nuevo_nombre
        else:
            print('Nombre inválido')  # acá debería generar una exepcion, pero no llegué.

    @edad.setter
    def edad(self, edad):
        try:
            int(edad)
            if edad > 0:
                self.__edad = edad
            else:
                print('Error, la edad debe ser mayor a cero')
        except ValueError:
            print('Error, valor inválido para la edad')

    @DNI.setter
    def DNI(self, dni):
        try:
            int(dni)
            if dni > 0:
                self.__dni = dni
            else:
                print('Error, el DNI no puede ser cero')
        except ValueError:
            print('Error, valor inválido para el DNI')

    def mostrar(self):
        print(f"Mi nombre es: {self.nombre}, mi edad es {self.edad} años y mi DNI es {self.DNI}")

    def es_mayor_de_edad(self):
        return (self.edad >= 18)

