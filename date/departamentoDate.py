from date.connection import MySQLConnection


#Esta clase me permite hacer todas las consultas a la base de datos que tengan que ver con el empleado
class DepartamentoDate():
    
    
    def buscar_departamento(self, departamento_id):
        # Crear una instancia de MySQLConnection y establecer la conexión
        connection = MySQLConnection()
        connection.connect()

        # Construir la consulta SQL utilizando el ID del empleado proporcionado
        query = f"SELECT * FROM departamento WHERE dep_id = {departamento_id}"

        try:

            result = connection.execute_query(query)
            return result

        except Exception as E:

            print("entra a el error")
            return E
        
                
        finally:
            # Cerrar la conexión con la base de datos en cualquier caso
            connection.disconnect()
    
    def agregar_departamento(self, id, nombre, poblacion):

        connection = MySQLConnection()
        connection.connect()

        # Construir la consulta SQL utilizando el ID del empleado proporcionado
        query = f"""
            INSERT INTO departamento (dep_id, nombre, cantidad_poblacion) 
	            VALUES ({id}, '{nombre}', '{poblacion}');
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

    def eliminar_departamento(self,dep_id):
        # Crear una instancia de MySQLConnection y establecer la conexión
        connection = MySQLConnection()
        connection.connect()

        # Construir la consulta SQL utilizando el ID del empleado proporcionado
        query = f"delete from departamento where dep_id = {dep_id};"
        

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


    def actualizar_departamento(self, id, nombre, poblacion):

        connection = MySQLConnection()
        connection.connect()

        # Construir la consulta SQL utilizando el ID del empleado proporcionado
        query = f"""
            UPDATE departamento
                SET nombre='{nombre}', cantidad_poblacion='{poblacion}'
                WHERE dep_id={id};
        """

        try:
            # Ejecutar la consulta SQL utilizando la conexión establecida
            connection.execute_query(query)
            connection.connection.commit()

        except Exception as E:
            return E
        
        finally:
            # Cerrar la conexión con la base de datos en cualquier caso
            connection.disconnect()

    def buscar_informacion(self, id=None, nombre=None, poblacion=None):
        #Esta funcion me permite buscar un empleado específico, o si estan llenos los parámetros de 
        #busqueda simplemente devuelve todos los empleados
        
        connection = MySQLConnection()
        connection.connect()

        condition = ""
        if id:
            condition += f"dep_id LIKE '%{id}%'"
        else:
            if id:
                if condition:
                    condition += f" and id LIKE '%{id}%'"
                else:
                    condition += f"id LIKE '%{id}%'"

            if nombre:
                if condition:
                    condition += f" and nombre LIKE '%{nombre}%'"
                else:
                    condition += f"nombre LIKE '%{nombre}%'"

            if poblacion:
                if condition:
                    condition += f" and cantidad_poblacion LIKE '%{poblacion}%'"
                else:
                    condition += f"cantidad_poblacion LIKE '%{poblacion}%'"


        if condition:
            # Construct SQL query for searching information with conditions
            query = f"""
                SELECT * FROM departamento WHERE {condition};
            """
        else:
            # Construct SQL query for searching all information
            query = f"""
                SELECT * FROM departamento;
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


    


