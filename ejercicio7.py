# 7. Crea una clase llamada Cuenta que tendrá los siguientes atributos: titular (que es una
#  persona) y cantidad (puede tener decimales). El titular será obligatorio y la cantidad es
#  opcional. Crear los siguientes métodos para la clase:
#   * Un constructor, donde los datos pueden estar vacíos.
#   * Los setters y getters para cada uno de los atributos. El atributo no se puede modificar
#       directamente, sólo ingresando o retirando dinero.
#   * mostrar(): Muestra los datos de la cuenta.
#   * ingresar(cantidad): se ingresa una cantidad a la cuenta, si la cantidad introducida es
#       negativa, no se hará nada.
#   * retirar(cantidad): se retira una cantidad a la cuenta. La cuenta puede estar en números
#       rojos.

from ejercicio6 import Persona;

class Cuenta:
    def __init__(self, un_titular = None, saldo_inicial = 0):
        self.titular = un_titular
        self.__saldo = 0
        self.ingresar(saldo_inicial)


    @property
    def titular(self):
        return self.__titular

    @property
    def saldo(self):
        return self.__saldo

    @titular.setter
    def titular(self, nuevo_titular):
        if isinstance(nuevo_titular, Persona):
            self.__titular = nuevo_titular
        else:
            print("Error en Persona titular")
            raise ValueError


    def ingresar(self, monto_credito):
        try:
            if monto_credito > 0:
                self.__saldo = self.__saldo + monto_credito
        except ValueError:
            print("Importe inválido a acreditar")

    def retirar(self, monto_debito):
        try:
            if monto_debito > 0:
                self.__saldo = self.__saldo - monto_debito
        except ValueError:
            print("Importe a debitar inválido")

    def mostrar(self):
        return f"El titular de la cuenta es: {self.titular.nombre}, y posee un saldo de: {self.saldo} pesos"


