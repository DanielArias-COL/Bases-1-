from date.connection import MySQLConnection


#Esta clase me permite hacer todas las consultas a la base de datos que tengan que ver con el empleado
class SucursalDate():
    
    
    def buscar_sucursal(self, sucursal_id):
        # Crear una instancia de MySQLConnection y establecer la conexión
        connection = MySQLConnection()
        connection.connect()

        # Construir la consulta SQL utilizando el ID del empleado proporcionado
        query = f"SELECT * FROM sucursal WHERE suc_id = {sucursal_id}"

        try:

            result = connection.execute_query(query)
            return result

        except Exception as E:

            print("entra a el error")
            return E
        
                
        finally:
            # Cerrar la conexión con la base de datos en cualquier caso
            connection.disconnect()
    
    def agregar_sucursal(self, suc_id, nombre, presupuesto_anual, mun_id):

        connection = MySQLConnection()
        connection.connect()

        # Construir la consulta SQL utilizando el ID del empleado proporcionado
        query = f"""
            INSERT INTO sucursal (suc_id, nombre, presupuesto_anual, mun_id) 
	            VALUES ('{suc_id}', '{nombre}', '{presupuesto_anual}', '{mun_id}');
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

    def eliminar_sucursal(self,sucursal_id):
        # Crear una instancia de MySQLConnection y establecer la conexión
        connection = MySQLConnection()
        connection.connect()

        # Construir la consulta SQL utilizando el ID del empleado proporcionado
        query = f"delete from sucursal where suc_id = {sucursal_id};"
        

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


    def actualizar_sucursal(self, suc_id, nombre, presupuesto_anual, mun_id):

        connection = MySQLConnection()
        connection.connect()

        # Construir la consulta SQL utilizando el ID del empleado proporcionado
        query = f"""
            UPDATE sucursal
                SET nombre='{nombre}', presupuesto_anual='{presupuesto_anual}', mun_id='{mun_id}'
                WHERE suc_id={suc_id};
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

    def buscar_informacion(self, suc_id=None, nombre=None, presupuesto_anual=None, mun_id=None):
        #Esta funcion me permite buscar un empleado específico, o si estan llenos los parámetros de 
        #busqueda simplemente devuelve todos los empleados
        
        connection = MySQLConnection()
        connection.connect()

        condition = ""
        if suc_id:
            condition += f"suc_id LIKE '%{suc_id}%'"
        else:
            if nombre:
                if condition:
                    condition += f" and nombre LIKE '%{nombre}%'"
                else:
                    condition += f"nombre LIKE '%{nombre}%'"

            if presupuesto_anual:
                if condition:
                    condition += f" and presupuesto_anual LIKE '%{presupuesto_anual}%'"
                else:
                    condition += f"presupuesto_anual LIKE '%{presupuesto_anual}%'"

            if mun_id:
                if condition:
                    condition += f" and mun_id LIKE '%{mun_id}%'"
                else:
                    condition += f"mun_id LIKE '%{mun_id}%'"

           


        if condition:
            # Construct SQL query for searching information with conditions
            query = f"""
                SELECT * FROM sucursal WHERE {condition};
            """
        else:
            # Construct SQL query for searching all information
            query = f"""
                SELECT * FROM sucursal;
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


    


