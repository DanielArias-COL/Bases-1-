
from date.connection import MySQLConnection
from model.empleado import Empleado

class EmpleadoDate():
    
    def consultarEmpleados_tabla(self):
        empleados = []
        connection = MySQLConnection()
        connection.connect()

        # Ejecutar una consulta de ejemplo
        query = "SELECT * FROM empleado"
        result = connection.execute_query(query)

        # Recorrer los resultados y crear diccionarios
        for empleado_data in result:
            empleado_dict = {
                "Codigo": empleado_data[0],
                "Cedula": empleado_data[1],
                "Nombre": empleado_data[2],
                "Direccion": empleado_data[3],
                "Telefono": empleado_data[4]
                # Agrega más claves y valores según la estructura de la tabla 'empleado'
            }
            empleados.append(empleado_dict)

        connection.disconnect()

        return empleados

    def buscar_empleado(self, empleado_id):
        # Crear una instancia de MySQLConnection y establecer la conexión
        connection = MySQLConnection()
        connection.connect()

        # Construir la consulta SQL utilizando el ID del empleado proporcionado
        query = f"SELECT * FROM empleado WHERE emp_id = {empleado_id}"

        try:

            result = connection.execute_query(query)
            return result

        except Exception as E:

            print("entra a el error")
            return E
        
                
        finally:
            # Cerrar la conexión con la base de datos en cualquier caso
            connection.disconnect()
    
    def agregar_empleado(self, id, cedula, nombre, direccion, telefono):

        connection = MySQLConnection()
        connection.connect()

        # Construir la consulta SQL utilizando el ID del empleado proporcionado
        query = f"""
            INSERT INTO empleado (emp_id, cedula, nombre, direccion, telefono) 
	            VALUES ({id}, '{cedula}', '{nombre}', '{direccion}', '{telefono}');
        """
        try:
            # Ejecutar la consulta SQL utilizando la conexión establecida
            connection.execute_query(query)
            connection.connection.commit()

        except Exception as E:
            print("entro a el error")
            return E
        
        finally:
            # Cerrar la conexión con la base de datos en cualquier caso
            connection.disconnect()


    


