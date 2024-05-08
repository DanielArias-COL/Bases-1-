from date.connection import MySQLConnection


#Esta clase me permite hacer todas las consultas a la base de datos que tengan que ver con el empleado
class ListaSucDate():
    
    

    
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


   

    def buscar_informacion(self, sucursal_id=None):
        #Esta funcion me permite buscar un empleado específico, o si estan llenos los parámetros de 
        #busqueda simplemente devuelve todos los empleados
        
        connection = MySQLConnection()
        connection.connect()

        condition = ""
        if sucursal_id:
            condition += f"suc_id LIKE '%{sucursal_id}%'"

        
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


    


