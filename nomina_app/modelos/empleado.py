# En este módulo definimos las clases (modelos) del sistema de nómina.
# Se aplican conceptos de POO:
# - HERENCIA: clases hijas heredan de la clase base Empleado.
# - ENCAPSULACIÓN: atributos privados (por ejemplo, __salario_base, __tarifa_hora).
# - POLIMORFISMO: el método calcular_pago() se comporta distinto según el tipo de empleado.

class Empleado:
    """
    Clase base: representa un empleado de forma general.
    Sirve como "molde" para los distintos tipos de empleados.

    Polimorfismo:
    - calcular_pago() se define aquí de forma genérica,
      pero se sobrescribe en las clases hijas.
    """
    def __init__(self, nombre: str, cedula: str): # Constructor: inicializa los atributos básicos del empleado
        self.nombre = nombre
        self.cedula = cedula

    def calcular_pago(self) -> float: # Método base: se sobrescribe en las clases hijas para calcular el pago real
        return 0.0


