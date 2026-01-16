# main.py
# Archivo principal: crea instancias (objetos) y demuestra el funcionamiento.

from modelos.empleado import EmpleadoTiempoCompleto, EmpleadoPorHoras  # Importa las clases de empleados
from servicios.nomina import Nomina                                    # Importa la clase de nómina

# Función principal
def main():
    nomina = Nomina()  # Crea el sistema de nómina

    # INSTANCIACIÓN: creación de objetos
    empleado1 = EmpleadoTiempoCompleto("Verónica Jiménez", "0102030405", salario_base=500, bono=50)
    empleado2 = EmpleadoPorHoras("Luis Andrade", "0912345678", tarifa_hora=3.5, horas_trabajadas=120)

    # Agregar al sistema (servicio)
    nomina.agregar_empleado(empleado1)  # Agrega el empleado 1
    nomina.agregar_empleado(empleado2)

    print("LISTA DE EMPLEADOS")   # Muestra la lista de empleados registrados
    nomina.listar_empleados()

    print("\nPAGOS (POLIMORFISMO)")  # Muestra los pagos calculados para cada empleado
    nomina.pagar_todos()

    # ENCAPSULACIÓN (prueba): modificar datos privados solo con métodos
    print("\nCAMBIO DE SALARIO BASE (ENCAPSULACIÓN)")
    empleado1.cambiar_salario_base(550)               # Cambia el salario base usando el setter
    print(empleado1.mostrar_informacion())            # Muestra la información actualizada
    print(f"Nuevo pago de {empleado1.nombre}: ${empleado1.calcular_pago():.2f}")

if __name__ == "__main__":
    main()  # Ejecuta la función principal
