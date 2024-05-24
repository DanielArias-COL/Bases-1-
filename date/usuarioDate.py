from date.connection import MySQLConnection


#Esta clase me permite hacer todas las consultas a la base de datos que tengan que ver con el empleado
class UsuarioDate():
    

    def lista_auditoria_por_usuario(self):
        connection = MySQLConnection()
        connection.connect()

        # Construir la consulta SQL utilizando el ID del empleado proporcionado
        query = (
        "SELECT u.nombre_alternativo AS usuario, "
        "COUNT(CASE WHEN ae.fecha_salida IS NULL THEN 1 END) AS auditorias_entrada, "
        "COUNT(CASE WHEN ae.fecha_salida IS NOT NULL THEN 1 END) AS auditorias_salida "
        "FROM Usuario u "
        "LEFT JOIN AuditoriaES ae ON u.usr_id = ae.usr_id "
        "GROUP BY u.nombre_alternativo"
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
    



    def obtener_usuario_nombre(self, nombre):
        connection = MySQLConnection()
        connection.connect()

        # Construir la consulta SQL utilizando el ID del empleado proporcionado
        query = f"SELECT * FROM usuario WHERE nombre_alternativo = '{nombre}'"

        try:

            result = connection.execute_query(query)
            return result

        except Exception as E:

            print("entra a el error")
            return E
        
                
        finally:
            # Cerrar la conexión con la base de datos en cualquier caso
            connection.disconnect()
    

    def buscar_usuario(self, usuario_id):
        # Crear una instancia de MySQLConnection y establecer la conexión
        connection = MySQLConnection()
        connection.connect()

        # Construir la consulta SQL utilizando el ID del empleado proporcionado
        query = f"SELECT * FROM usuario WHERE usr_id = {usuario_id}"

        try:

            result = connection.execute_query(query)
            return result

        except Exception as E:

            print("entra a el error")
            return E
        
                
        finally:
            # Cerrar la conexión con la base de datos en cualquier caso
            connection.disconnect()
    
    def agregar_usuario(self, usr_id, nombre_alternativo, clave, nivel_usuario):

        connection = MySQLConnection()
        connection.connect()

        # Construir la consulta SQL utilizando el ID del empleado proporcionado
        query = f"""
            INSERT INTO usuario (usr_id, nombre_alternativo, clave, nivel_usuario) 
	            VALUES ('{usr_id}', '{nombre_alternativo}', '{clave}', '{nivel_usuario}');
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

    def eliminar_usuario(self,usuario_id):
        # Crear una instancia de MySQLConnection y establecer la conexión
        connection = MySQLConnection()
        connection.connect()

        # Construir la consulta SQL utilizando el ID del empleado proporcionado
        query = f"delete from usuario where usr_id = {usuario_id};"
        

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


    def actualizar_usuario(self, usr_id, nombre_alternativo, clave, nivel_usuario):

        connection = MySQLConnection()
        connection.connect()

        # Construir la consulta SQL utilizando el ID del empleado proporcionado
        query = f"""
            UPDATE usuario
                SET nombre_alternativo='{nombre_alternativo}', clave='{clave}', nivel_usuario='{nivel_usuario}'
                WHERE usr_id={usr_id};
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

    def buscar_informacion(self, usr_id=None, nombre_alternativo=None, clave=None, nivel_usuario=None):
        #Esta funcion me permite buscar un empleado específico, o si estan llenos los parámetros de 
        #busqueda simplemente devuelve todos los empleados
        
        connection = MySQLConnection()
        connection.connect()

        condition = ""
        if usr_id:
            condition += f"usr_id LIKE '%{usr_id}%'"
        else:
            if nombre_alternativo:
                if condition:
                    condition += f" and nombre_alternativo LIKE '%{nombre_alternativo}%'"
                else:
                    condition += f"nombre_alternativo LIKE '%{nombre_alternativo}%'"

            if clave:
                if condition:
                    condition += f" and clave LIKE '%{clave}%'"
                else:
                    condition += f"clave LIKE '%{clave}%'"

            if nivel_usuario != "Seleccionar":
                if condition:
                    condition += f" and nivel_usuario LIKE '%{nivel_usuario}%'"
                else:
                    condition += f"nivel_usuario LIKE '%{nivel_usuario}%'"

           


        if condition:
            # Construct SQL query for searching information with conditions
            query = f"""
                SELECT * FROM usuario WHERE {condition};
            """
        else:
            # Construct SQL query for searching all information
            query = f"""
                SELECT * FROM usuario;
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


    


