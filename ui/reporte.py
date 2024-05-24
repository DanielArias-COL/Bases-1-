from PyQt6 import uic 
import tkinter as tk
from tkinter import filedialog
import datetime

from reportlab.lib.pagesizes import letter
from reportlab.lib.colors import gray, beige, black
from reportlab.pdfgen import canvas
from date.connection import MySQLConnection


from PyQt6.QtWidgets import QDialog
from date.sucursalDate import SucursalDate
from date.empleadoDate import EmpleadoDate
from date.departamentoDate import DepartamentoDate
from date.municipioDate import MunicipioDate
from date.cargoDate import CargoDate
from date.profesionDate import ProfesionDate
from date.contratoDate import ContratoDate
from date.usuarioDate import UsuarioDate







class VentanaGestorInformes(QDialog):
    def __init__(self, ventanaMenu, nivel_usuario):
        super().__init__()
        self.ui = uic.loadUi('ui\gestor_reportes_form.ui',self)
        self.nivel_usuario = nivel_usuario
        self.ventana_menu= ventanaMenu
        self.ventana_menu.hide()

        #conectamos la UI a las variables de la clase.
        self.comboBox = self.ui.comboBox
        # PySide2.QtWidgets.QComboBox.clearEditText()¶
        # Crear una lista de cadenas
        lista_cadenas = self.asignar_reportes()
        self.comboBox.addItems(lista_cadenas)



        
        # Initialize signal-slot connections
        self.init_signal_slot()
        #Instancia para hacer consultas a la base de datos
        self.sucursal_date = SucursalDate()
        self.empleado_date = EmpleadoDate()
        self.departamento_date = DepartamentoDate()
        self.municipio_date = MunicipioDate()
        self.cargo_date = CargoDate()
        self.profesion_date = ProfesionDate()
        self.contrato_date = ContratoDate()
        self.usuario_date = UsuarioDate()
        
        #self.buscar_registro()
        self.ui.show()


    def init_signal_slot(self):
        # Conección de los botones a sus respectivas funciones
        self.guardarComo_btn.clicked.connect(self.guardar_como)        
        self.back_btn.clicked.connect(self.regresar_atras)
        

    def asignar_reportes(self):

        lista_cadenas = ""
        if self.nivel_usuario == "Principal":
            lista_cadenas = ["Cantidad de contratos por sucursal",
                             "Número de auditorías de entrada y salida por usuario"]
            
        if self.nivel_usuario == "Paramétrico":
            lista_cadenas = ["Salario promedio por cargo",
                             "Número de empleados por departamento"]
            
        if self.nivel_usuario == "Esporádico":
            lista_cadenas = ["Cantidad de empleados por profesión",
                             "Empleados que trabajan en sucursales de Medellín"]
            

        return  lista_cadenas
        
    def guardar_como(self):

        if (self.comboBox.currentText() == "Cantidad de contratos por sucursal"):
            query = self.contrato_date.empleados_por_departamento() 
            self.generar_reporte_pdf(query, "cantidad de contratos por sucursal")

        if (self.comboBox.currentText() == "Número de auditorías de entrada y salida por usuario"):
            query = self.usuario_date.lista_auditoria_por_usuario() 
            self.generar_reporte_pdf(query, "Número de auditorías de entrada y salida por usuario")

        
        if (self.comboBox.currentText() == "Salario promedio por cargo"):
            query = self.cargo_date.salario_promedio_por_cargo() 
            self.generar_reporte_pdf(query, "Salario promedio por cargo")

        
        if (self.comboBox.currentText() == "Número de empleados por departamento"):
            query = self.empleado_date.emplados_por_departamento() 
            self.generar_reporte_pdf(query, "Número de empleados por departamento")   

        
        if (self.comboBox.currentText() == "Cantidad de empleados por profesión"):
            query = self.empleado_date.cantidad_empleados_por_profesion() 
            self.generar_reporte_pdf(query, "Cantidad de empleados por profesión")

        
        if (self.comboBox.currentText() == "Empleados que trabajan en sucursales de Medellín"):
            query = self.empleado_date.empleados_de_medellin() 
            self.generar_reporte_pdf(query, "Empleados que trabajan en Medellín")

      
        




    def seleccionar_carpeta(self):
        # Crear una ventana
        ventana = tk.Tk()
        ventana.withdraw()
        directorio = filedialog.askdirectory()
        if directorio:
            print("Carpeta seleccionada:", directorio)
        else:
            print("No se seleccionó ninguna carpeta.")    

        return directorio        

    


    def generar_reporte_pdf(self, result, nombrePDF):
        direccion = self.seleccionar_carpeta()
        
        if result:
            # Crear el documento PDF
            pdf_path = f"{direccion}/{nombrePDF}.pdf"  # Ruta completa al archivo PDF
            
            # Crear el lienzo (canvas) del PDF
            c = canvas.Canvas(pdf_path, pagesize=letter)
            
            # Agregar el título
            titulo = f"Reporte {nombrePDF}"
            c.setFont("Helvetica-Bold", 16)
            c.drawString(200, 750, titulo)
            
            # Agregar la fecha actual
            fecha_actual = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            c.setFont("Helvetica", 12)
            c.drawString(200, 730, f"Fecha de creación: {fecha_actual}")
            
            # Definir los datos de la tabla
            data = [list(result[0])]  # Utilizamos la primera tupla para obtener los nombres de las columnas
            for fila in result:
                data.append(list(fila))
            
            # Definir el tamaño de la tabla
            num_filas = len(data)
            num_columnas = len(data[0])
            ancho_celda = 130
            alto_celda = 20
            ancho_tabla = ancho_celda * num_columnas
            alto_tabla = alto_celda * num_filas
            
            # Dibujar la tabla
            for i, fila in enumerate(data):
                for j, valor in enumerate(fila):
                    x = j * ancho_celda
                    y = 700 - (i * alto_celda)  # Ajustar la posición vertical
                    c.drawString(x + 5, y - 15, str(valor))  # Dibujar el valor en la celda
            
            # Dibujar los bordes de la tabla
            for i in range(num_filas + 1):
                c.line(0, 700 - (i * alto_celda), ancho_tabla, 700 - (i * alto_celda))  # Dibujar las líneas horizontales
            for j in range(num_columnas + 1):
                c.line(j * ancho_celda, 700, j * ancho_celda, 700 - alto_tabla)  # Dibujar las líneas verticales
            
            # Guardar el PDF
            c.save()
            
            print("El reporte ha sido generado y guardado en:", pdf_path)
        else:
            print("No se encontraron resultados para generar el reporte.")

            
    def regresar_atras(self):
        from ui.menu import VentanaMenu
        self.ventana_menu.show()
        self.close()  