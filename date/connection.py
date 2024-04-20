#conexion a la base de datos sql

import mysql.connector

class MySQLConnection:
    #modificar segun caracteristicas propias
    def __init__(self):
        self.host = 'localhost'
        self.user = 'root'
        self.password = 'Heropro.12'
        self.database = 'Banco'
        self.connection = None

    def connect(self):
        try:
            self.connection = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database
            )
            print("Conexión establecida correctamente.")
        except mysql.connector.Error as e:
            print(f"Error al conectarse a la base de datos: {e}")

    def disconnect(self):
        if self.connection:
            self.connection.close()
            print("Conexión cerrada.")

    def execute_query(self, query):
        cursor = self.connection.cursor()
        try:
            cursor.execute(query)
            result = cursor.fetchall()
            return result
        except mysql.connector.Error as e:
            print(f"Error al ejecutar la consulta: {e}")
        finally:
            cursor.close()


