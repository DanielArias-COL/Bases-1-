
from date.connection import MySQLConnection


#Esta clase me permite hacer todas las consultas a la base de datos que tengan que ver con el empleado
class EmpleadoDate():

    def empleados_de_medellin(self):
        # Crear una instancia de MySQLConnection y establecer la conexión
        connection = MySQLConnection()
        connection.connect()

        # Construir la consulta SQL utilizando el ID del empleado proporcionado
        query = (
        "SELECT e.emp_id, e.cedula, e.nombre, e.direccion, e.telefono, s.nombre AS sucursal, m.nombre AS municipio "
        "FROM Empleado e "
        "INNER JOIN Contrato c ON e.emp_id = c.emp_id "
        "INNER JOIN Sucursal s ON c.suc_id = s.suc_id "
        "INNER JOIN Municipio m ON s.mun_id = m.mun_id "
        "WHERE m.nombre = 'Medellín'"
        )


        try:

            result = connection.execute_query(query)
            return result

        except Exception as E:

            print("entra a el error")
            return E
        
                
        finally:
            # Cerrar la conexión con la base de datos en cualquier caso
            connection.disconnect()
    def cantidad_empleados_por_profesion(self): 
        # Crear una instancia de MySQLConnection y establecer la conexión
        connection = MySQLConnection()
        connection.connect()

        # Construir la consulta SQL utilizando el ID del empleado proporcionado
        query = (
            "SELECT p.nombre AS profesion, "
            "COUNT(dep.emp_id) AS cantidad_empleados "
            "FROM Profesion p "
            "LEFT JOIN Detalle_Empleado_Profesion dep ON p.prf_id = dep.prf_id "
            "GROUP BY p.nombre"
        )


        try:

            result = connection.execute_query(query)
            return result

        except Exception as E:

            print("entra a el error")
            return E
               
        finally:
            # Cerrar la conexión con la base de datos en cualquier caso
            connection.disconnect()
    


    def emplados_por_departamento(self):
        # Crear una instancia de MySQLConnection y establecer la conexión
        connection = MySQLConnection()
        connection.connect()

        # Construir la consulta SQL utilizando el ID del empleado proporcionado
        query = (
        "SELECT d.nombre AS departamento, "
        "COUNT(e.emp_id) AS cantidad_empleados "
        "FROM Departamento d "
        "LEFT JOIN Municipio m ON d.dep_id = m.dep_id "
        "LEFT JOIN Sucursal s ON m.mun_id = s.mun_id "
        "LEFT JOIN Contrato c ON s.suc_id = c.suc_id "
        "LEFT JOIN Empleado e ON c.emp_id = e.emp_id "
        "GROUP BY d.nombre"
        )




        try:

            result = connection.execute_query(query)
            return result

        except Exception as E:

            print("entra a el error")
            return E
        
                
        finally:
            # Cerrar la conexión con la base de datos en cualquier caso
            connection.disconnect()
    


    
    def clasificar_por_profesion(self, profesion):
        # Crear una instancia de MySQLConnection y establecer la conexión
        connection = MySQLConnection()
        connection.connect()

        # Construir la consulta SQL utilizando el ID del empleado proporcionado
        query = f"SELECT e.emp_id, e.cedula, e.nombre, e.direccion, e.telefono FROM empleado e \
          INNER JOIN  detalle_empleado_profesion dep \
          ON e.emp_id = dep.emp_id \
          INNER JOIN  profesion p \
          ON p.prf_id = dep.prf_id \
          WHERE p.nombre = '{profesion}'"



        try:

            result = connection.execute_query(query)
            return result

        except Exception as E:

            print("entra a el error")
            return E
        
                
        finally:
            # Cerrar la conexión con la base de datos en cualquier caso
            connection.disconnect()
    


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

    def eliminar_empleado(self,empleado_id):
        # Crear una instancia de MySQLConnection y establecer la conexión
        connection = MySQLConnection()
        connection.connect()

        # Construir la consulta SQL utilizando el ID del empleado proporcionado
        query = f"delete from empleado where emp_id = {empleado_id};"
        

        try:

            # Ejecutar la consulta SQL utilizando la conexión establecida
            resresultult=connection.execute_query(query)
            connection.connection.commit()
            return resresultult

        except Exception as E:

            return E
        
                
        finally:
            # Cerrar la conexión con la base de datos en cualquier caso
            connection.disconnect()


    def actualizar_empleado(self, id, cedula, nombre, direccion, telefono):

        connection = MySQLConnection()
        connection.connect()

        # Construir la consulta SQL utilizando el ID del empleado proporcionado
        query = f"""
            UPDATE empleado
                SET cedula='{cedula}', nombre='{nombre}', direccion='{direccion}', telefono='{telefono}'
                WHERE emp_id={id};
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

    def buscar_informacion(self, id=None, cedula=None, nombre=None, direccion=None, telefono=None):
        #Esta funcion me permite buscar un empleado específico, o si estan llenos los parámetros de 
        #busqueda simplemente devuelve todos los empleados
        
        connection = MySQLConnection()
        connection.connect()

        condition = ""
        if id:
            condition += f"emp_id LIKE '%{id}%'"
        else:
            if cedula:
                if condition:
                    condition += f" and cedula LIKE '%{cedula}%'"
                else:
                    condition += f"cedula LIKE '%{cedula}%'"

            if nombre:
                if condition:
                    condition += f" and nombre LIKE '%{nombre}%'"
                else:
                    condition += f"nombre LIKE '%{nombre}%'"

            if direccion:
                if condition:
                    condition += f" and nombre LIKE '%{direccion}%'"
                else:
                    condition += f"nombre LIKE '%{direccion}%'"

            if telefono:
                if condition:
                    condition += f"  and nombre LIKE '%{telefono}%'"
                else:
                    condition += f"nombre LIKE '%{telefono}%'"


        if condition:
            # Construct SQL query for searching information with conditions
            query = f"""
                SELECT * FROM empleado WHERE {condition};
            """
        else:
            # Construct SQL query for searching all information
            query = f"""
                SELECT * FROM empleado;
             """

        try:
            # Execute the SQL query for searching information
            #self.cursor.execute(sql)
            #result = self.cursor.fetchall()
            result = connection.execute_query(query)
            return result

        except Exception as E:
            return E

        finally:
            # Close the database connection
            connection.disconnect()


    


