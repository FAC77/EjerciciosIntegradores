# 8. Vamos a definir ahora una “Cuenta Joven”, para ello vamos a crear una nueva clase
#    CuantaJoven que deriva de la clase creada en el punto 7. Cuando se crea esta nueva clase,
#    además del titular y la cantidad se debe guardar una bonificación que estará expresada en
#    tanto por ciento. Crear los siguientes métodos para la clase:
#       * Un constructor.
#       * Los setters y getters para el nuevo atributo.
#       * En esta ocasión los titulares de este tipo de cuenta tienen que ser mayor de edad, por lo
#           tanto hay que crear un método es_titular_valido() que devuelve verdadero si el titular
#           es mayor de edad pero menor de 25 años y falso en caso contrario.
#       * Además, la retirada de dinero sólo se podrá hacer si el titular es válido.
#       * El método mostrar() debe devolver el mensaje de “Cuenta Joven” y la bonificación de la
#         cuenta.

from ejercicio7 import Cuenta
from ejercicio6 import Persona

class CuentaJoven(Cuenta):
    def __init__(self, un_titular=None, saldo_inicial=0, bonificacion = 0):
        super().__init__(un_titular, saldo_inicial)
        self.bonificacion = bonificacion

    @property
    def bonificacion(self):
        return self.__bonificacion

    @bonificacion.setter
    def bonificacion(self, una_bonificacaion):
        self.__bonificacion = una_bonificacaion

    def es_titular_valido(self, persona):
        return(self.__es_persona_valida(persona))


    def retirar(self, monto_debito):
        try:
            if monto_debito > 0 and self.es_titular_valido(self.titular):
                self.__saldo = self.__saldo - monto_debito
            else:
                print("El titular es inválido para retirar")
        except ValueError:
            print("Importe a debitar inválido")

    def mostrar(self):
        return f"Cuenta Joven, con una bonificación de: {self.bonificacion} %"


    @Cuenta.titular.setter
    def titular(self, nuevo_titular):
        if isinstance(nuevo_titular, Persona) and self.es_titular_valido(nuevo_titular):
            self.__titular = nuevo_titular
        else:
            print("Error en Persona titular")
            raise ValueError

    def __es_persona_valida(self, persona):
        return(persona.es_mayor_de_edad and persona.edad < 25)


