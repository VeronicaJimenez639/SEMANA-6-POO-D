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
    
    def mostrar_informacion(self) -> str: # Método para mostrar información básica del empleado
        return f"Empleado: {self.nombre}, Cédula: {self.cedula}"    

class EmpleadoTiempoCompleto(Empleado):
    """
    Clase hija: EmpleadoTiempoCompleto hereda de Empleado.

    Encapsulación:
    - __salario_base es privado, por lo que se accede/modifica mediante métodos.
    """
    def __init__(self, nombre: str, cedula: str, salario_base: float, bono: float = 0.0):
        super().__init__(nombre, cedula)                # super() llama al constructor de la clase padre (Empleado)
        self.__salario_base = salario_base              # Atributo privado: salario base
        self.bono = bono                                # Atributo público: bono adicional

    # Getter: permite obtener el salario base de forma controlada
    def obtener_salario_base(self) -> float:            
        return self.__salario_base

    # Setter: permite cambiar el salario base con validación
    def cambiar_salario_base(self, nuevo_salario: float) -> None:        
        if nuevo_salario > 0:                                            
            self.__salario_base = nuevo_salario                           
        else:
            print("El salario debe ser mayor que 0.")

    # Polimorfismo (sobreescritura):
    def calcular_pago(self) -> float:          # Para tiempo completo, el pago es salario base + bono
        return self.__salario_base + self.bono

    # Sobrescribe el método para mostrar información más completa
    def mostrar_informacion(self) -> str:
        return (
            f"{super().mostrar_informacion()}, "
            f"Tipo: Tiempo Completo, Base: {self.__salario_base}, Bono: {self.bono}."
        )
    
    

