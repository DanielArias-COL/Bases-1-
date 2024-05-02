from date.connection import MySQLConnection


#Esta clase me permite hacer todas las consultas a la base de datos que tengan que ver con el empleado
class MunicipioDate():
    
    
    def buscar_municipio(self, municipio_id):
        # Crear una instancia de MySQLConnection y establecer la conexión
        connection = MySQLConnection()
        connection.connect()

        # Construir la consulta SQL utilizando el ID del empleado proporcionado
        query = f"SELECT * FROM municipio WHERE mun_id = {municipio_id}"

        try:

            result = connection.execute_query(query)
            return result

        except Exception as E:

            print("entra a el error")
            return E
        
                
        finally:
            # Cerrar la conexión con la base de datos en cualquier caso
            connection.disconnect()
    
    def agregar_municipio(self, id, nombre, poblacion, dep_id, prd_id):

        connection = MySQLConnection()
        connection.connect()

        # Construir la consulta SQL utilizando el ID del empleado proporcionado
        query = f"""
            INSERT INTO municipio (mun_id, nombre, cantidad_poblacion, dep_id, prd_id) 
	            VALUES ({id}, '{nombre}', '{poblacion}', '{dep_id}', '{prd_id}');
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

    def eliminar_municipio(self,municipio_id):
        # Crear una instancia de MySQLConnection y establecer la conexión
        connection = MySQLConnection()
        connection.connect()

        # Construir la consulta SQL utilizando el ID del empleado proporcionado
        query = f"delete from municipio where mun_id = {municipio_id};"
        

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


    def actualizar_municipio(self, id, nombre, cantidad_poblacion, dep_id, prd_id):

        connection = MySQLConnection()
        connection.connect()

        # Construir la consulta SQL utilizando el ID del empleado proporcionado
        query = f"""
            UPDATE municipio
                SET nombre='{nombre}', cantidad_poblacion='{cantidad_poblacion}', dep_id='{dep_id}', prd_id='{prd_id}'
                WHERE mun_id={id};
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

    def buscar_informacion(self, id=None, nombre=None, poblacion=None, dep_id=None, prd_id=None):
        #Esta funcion me permite buscar un empleado específico, o si estan llenos los parámetros de 
        #busqueda simplemente devuelve todos los empleados
        
        connection = MySQLConnection()
        connection.connect()

        condition = ""
        if id:
            condition += f"mun_id LIKE '%{id}%'"
        else:
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

            if dep_id:
                if condition:
                    condition += f" and dep_id LIKE '%{dep_id}%'"
                else:
                    condition += f"dep_id LIKE '%{dep_id}%'"

            if prd_id:
                if condition:
                    condition += f"  and prd_id LIKE '%{prd_id}%'"
                else:
                    condition += f"prd_id LIKE '%{prd_id}%'"


        if condition:
            # Construct SQL query for searching information with conditions
            query = f"""
                SELECT * FROM municipio WHERE {condition};
            """
        else:
            # Construct SQL query for searching all information
            query = f"""
                SELECT * FROM municipio;
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


    


