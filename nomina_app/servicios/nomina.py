# servicios/nomina.py
# Lógica del sistema (servicios): # Aquí se administra la lista de empleados y se calcula la nómina total.

class Nomina: 
    """
    Clase Nomina:
    Administra una colección (lista) de empleados y permite:
    - Registrar empleados.
    - Listarlos.
    - Calcular y mostrar el pago total.

    Aquí se evidencia POLIMORFISMO cuando se llama calcular_pago()
    para distintos tipos de empleados (TiempoCompleto / PorHoras).
    """

    def __init__(self):     # Constructor: crea la lista donde se almacenarán los empleados
        self.empleados = []   

    def agregar_empleado(self, empleado) -> None:  # Método para agregar un empleado a la lista
        self.empleados.append(empleado)

    def listar_empleados(self) -> None:     # Método para listar todos los empleados registrados
        for e in self.empleados:            # Itera sobre la lista e imprime la información de cada empleado
            print(e.mostrar_informacion())  # Llama al método mostrar_informacion() de cada empleado

    def pagar_todos(self) -> None:
        """
        Calcula e imprime el pago individual de cada empleado y el total general.

        POLIMORFISMO:
        - Se utiliza el mismo método calcular_pago() para todos.
        - Cada empleado calcula su pago según su clase (sobreescritura).
        """
        total = 0.0  # Acumulador del total de la nómina

        for e in self.empleados:
            pago = e.calcular_pago()  # Pago calculado según el tipo de empleado
            total += pago             # Se suma al total general
            print(f"{e.nombre} cobra: ${pago:.2f}")

        # Al final se muestra el total a pagar en la nómina
        print(f"Total a pagar en nómina: ${total:.2f}")
