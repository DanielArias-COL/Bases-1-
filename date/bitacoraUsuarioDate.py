from date.connection import MySQLConnection
from datetime import datetime


#Esta clase me permite hacer todas las consultas a la base de datos que tengan que ver con el empleado
class BitacoraUsuarioDate():
    
    
    def agregar_bitacora(self, fecha_entrada=None, usr_id=None):

        connection = MySQLConnection()
        connection.connect()


        fecha_salida = self.obtener_fecha()
        # Construir la consulta SQL utilizando el ID del empleado proporcionado
        query = f"""
            INSERT INTO auditoriaes (fecha_entrada, fecha_salida, usr_id ) 
	            VALUES ('{fecha_entrada}', '{fecha_salida}', '{usr_id}');
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

    
    def buscar_informacion(self, bitacora_id=None):
        #Esta funcion me permite buscar un empleado específico, o si estan llenos los parámetros de 
        #busqueda simplemente devuelve todos los empleados
        
        connection = MySQLConnection()
        connection.connect()

        condition = ""
        if bitacora_id:
            condition += f"aud_id LIKE '%{bitacora_id}%'"

        
        if condition:
            # Construct SQL query for searching information with conditions
            query = f"""
                SELECT * FROM auditoriaes WHERE {condition};
            """
        else:
            # Construct SQL query for searching all information
            query = f"""
                SELECT * FROM auditoriaes;
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

    def obtener_fecha(self):
        # Obtener la fecha y hora actual
        fecha_actual = datetime.now()

        # Convertir la fecha y hora actual al formato de texto 'YYYY-MM-DD HH:MM:SS'
        fecha_entrada = fecha_actual.strftime('%Y-%m-%d %H:%M:%S') 

        return fecha_entrada       


    


