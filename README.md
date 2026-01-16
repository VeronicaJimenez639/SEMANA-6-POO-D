# nomina_app

Aplicación de un sistema de nómina en Python, desarrollada con Programación Orientada a Objetos (POO).
Permite registrar empleados y calcular sus pagos según su tipo (tiempo completo o por horas), aplicando herencia, encapsulación y polimorfismo.

## Características:

- **Herencia:** clase base `Empleado` y clases derivadas `EmpleadoTiempoCompleto` y `EmpleadoPorHoras`.
- **Encapsulación:** atributos privados como `__salario_base` y `__tarifa_hora`, con métodos para acceder y modificar.
- **Polimorfismo:** el método `calcular_pago()` se sobrescribe y calcula el pago según el tipo de empleado.
