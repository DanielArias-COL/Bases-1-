from date.connection import MySQLConnection


#Esta clase me permite hacer todas las consultas a la base de datos que tengan que ver con el empleado
class ContratoDate():
    
    
    def buscar_contrato(self, contrato_id):
        # Crear una instancia de MySQLConnection y establecer la conexión
        connection = MySQLConnection()
        connection.connect()

        # Construir la consulta SQL utilizando el ID del empleado proporcionado
        query = f"SELECT * FROM contrato WHERE contrato_id = {contrato_id}"

        try:

            result = connection.execute_query(query)
            return result

        except Exception as E:

            print("entra a el error")
            return E
        
                
        finally:
            # Cerrar la conexión con la base de datos en cualquier caso
            connection.disconnect()
    
    def agregar_contrato(self, contr_id, fecha_inicio, fecha_fin, emp_id, suc_id, carg_id):

        connection = MySQLConnection()
        connection.connect()

        # Construir la consulta SQL utilizando el ID del empleado proporcionado
        query = f"""
            INSERT INTO contrato (contr_id, fecha_inicio, fecha_fin, emp_id, suc_id, carg_id) 
	            VALUES ({contr_id}, '{fecha_inicio}', '{fecha_fin}', '{emp_id}', '{suc_id}', '{carg_id}');
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

    def eliminar_contrato(self,contrato_id):
        # Crear una instancia de MySQLConnection y establecer la conexión
        connection = MySQLConnection()
        connection.connect()

        # Construir la consulta SQL utilizando el ID del empleado proporcionado
        query = f"delete from contrato where contr_id = {contrato_id};"
        

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


    def actualizar_contrato(self, id, cedula, nombre, direccion, telefono):

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

    def buscar_informacion(self, contr_id=None, fecha_inicio=None, fecha_fin=None, emp_id=None, suc_id=None, carg_id=None):
        #Esta funcion me permite buscar un empleado específico, o si estan llenos los parámetros de 
        #busqueda simplemente devuelve todos los empleados
        
        connection = MySQLConnection()
        connection.connect()

        condition = ""
        if contr_id:
            condition += f"contr_id LIKE '%{contr_id}%'"
        else:
            if fecha_inicio:
                if condition:
                    condition += f" and fecha_inicio LIKE '%{fecha_inicio}%'"
                else:
                    condition += f"fecha_inicio LIKE '%{fecha_inicio}%'"

            if fecha_fin:
                if condition:
                    condition += f" and fecha_fin LIKE '%{fecha_fin}%'"
                else:
                    condition += f"fecha_fin LIKE '%{fecha_fin}%'"

            if emp_id:
                if condition:
                    condition += f" and emp_id LIKE '%{emp_id}%'"
                else:
                    condition += f"emp_id LIKE '%{emp_id}%'"

            if suc_id:
                if condition:
                    condition += f"  and suc_id LIKE '%{suc_id}%'"
                else:
                    condition += f"suc_id LIKE '%{suc_id}%'"

            if carg_id:
                if condition:
                    condition += f"  and carg_id LIKE '%{carg_id}%'"
                else:
                    condition += f"carg_id LIKE '%{carg_id}%'"


        if condition:
            # Construct SQL query for searching information with conditions
            query = f"""
                SELECT * FROM contrato WHERE {condition};
            """
        else:
            # Construct SQL query for searching all information
            query = f"""
                SELECT * FROM contrato;
             """

        try:
            # Execute the SQL query for searching information
            result = connection.execute_query(query)
            return result

        except Exception as E:
            return E

        finally:
            # Close the database connection
            connection.disconnect()


    


