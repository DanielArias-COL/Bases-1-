
from connection import MySQLConnection
from model.empleado import Empleado

class EmpleadoDate():
    
    def consultarEmpleados():
        empleados = []
        connection = MySQLConnection()
        connection.connect()

        # Ejecutar una consulta de ejemplo
        query = "SELECT * FROM empleado"
        result = connection.execute_query(query)

        # Recorrer los resultados y crear instancias de Empleado
        for empleado_data in result:
            empleado = Empleado(*empleado_data)
            empleados.append(empleado)

        connection.disconnect()

        return empleados

# Ejemplo de uso:
if __name__ == "__main__":
    lista_empleados = EmpleadoDate.consultarEmpleados()

    for empleado in lista_empleados:
        print(empleado._nombre)  # Acceder al nombre del empleado
