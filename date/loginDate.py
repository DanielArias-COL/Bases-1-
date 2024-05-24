from date.connection import MySQLConnection


#Esta clase me permite hacer todas las consultas a la base de datos que tengan que ver con el empleado
class LoginDate():
    
    
    def validar_usuario(self, usuario, clave):
        # Crear una instancia de MySQLConnection y establecer la conexión
        connection = MySQLConnection()
        connection.connect()

        # Construir la consulta SQL utilizando el ID del empleado proporcionado
        query=f"SELECT nombre_alternativo, clave FROM usuario WHERE nombre_alternativo='{usuario}' and clave='{clave}';"
        

        try:

            result = connection.execute_query(query)
            return result

        except Exception as E:

            print("entra a el error")
            return E
        
                
        finally:
            # Cerrar la conexión con la base de datos en cualquier caso
            connection.disconnect()