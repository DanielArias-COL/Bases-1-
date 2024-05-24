from date.connection import MySQLConnection


#Esta clase me permite hacer todas las consultas a la base de datos que tengan que ver con el cargo
class CargoDate():
    
    def salario_promedio_por_cargo(self):
        # Crear una instancia de MySQLConnection y establecer la conexión
        connection = MySQLConnection()
        connection.connect()

        # Construir la consulta SQL utilizando el ID del empleado proporcionado
        query = (
                "SELECT c.nombre AS cargo, "
                "AVG(c.salario) AS salario_promedio "
                "FROM Cargo c "
                "GROUP BY c.nombre"
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
    
        
        

    def filtrar_salario(self, valor, signo):
        # Crear una instancia de MySQLConnection y establecer la conexión
        connection = MySQLConnection()
        connection.connect()

        if signo == 0 :
            
            query = f"SELECT * FROM banco.cargo c where c.salario > {valor}"
            

        if signo == 1 :
            query = f"SELECT * FROM banco.cargo c where c.salario < {valor}"
            
        try:

            result = connection.execute_query(query)
            return result

        except Exception as E:

            print("entra a el error")
            return E
        
                
        finally:
            # Cerrar la conexión con la base de datos en cualquier caso
            connection.disconnect()


    
    def buscar_Cargo(self, cargo_id):
        # Crear una instancia de MySQLConnection y establecer la conexión
        connection = MySQLConnection()
        connection.connect()

        # Construir la consulta SQL utilizando el ID del empleado proporcionado
        query = f"SELECT * FROM cargo WHERE carg_id = {cargo_id}"

        try:

            result = connection.execute_query(query)
            return result

        except Exception as E:

            print("entra a el error")
            return E
        
                
        finally:
            # Cerrar la conexión con la base de datos en cualquier caso
            connection.disconnect()
    
    def agregar_Cargo(self, carg_id, nombre, salario):

        connection = MySQLConnection()
        connection.connect()

        # Construir la consulta SQL utilizando el ID del empleado proporcionado
        query = f"""
            INSERT INTO cargo (carg_id, nombre, salario) 
	            VALUES ({carg_id}, '{nombre}', '{salario}');
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

    def eliminar_Cargo(self,cargo_id):
        # Crear una instancia de MySQLConnection y establecer la conexión
        connection = MySQLConnection()
        connection.connect()

        # Construir la consulta SQL utilizando el ID del empleado proporcionado
        query = f"delete from cargo where carg_id = {cargo_id};"
        

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


    def actualizar_Cargo(self, carg_id, nombre, salario):

        connection = MySQLConnection()
        connection.connect()

        # Construir la consulta SQL utilizando el ID del empleado proporcionado
        query = f"""
            UPDATE cargo
                SET carg_id='{carg_id}', nombre='{nombre}', salario='{salario}'
                WHERE carg_id={carg_id};
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

    def buscar_informacion(self, suc_id=None, nombre=None, salario=None):
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

            if nombre:
                if condition:
                    condition += f" and nombre LIKE '%{nombre}%'"
                else:
                    condition += f"nombre LIKE '%{nombre}%'"

            if salario:
                if condition:
                    condition += f" and salario LIKE '%{salario}%'"
                else:
                    condition += f"salario LIKE '%{salario}%'"

           

        if condition:
            # Construct SQL query for searching information with conditions
            query = f"""
                SELECT * FROM cargo WHERE {condition};
            """
        else:
            # Construct SQL query for searching all information
            query = f"""
                SELECT * FROM cargo;
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


    


