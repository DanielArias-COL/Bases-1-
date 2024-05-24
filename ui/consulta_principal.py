from PyQt6 import uic 

from PyQt6.QtWidgets import QDialog, QTableWidgetItem, QPushButton, QMessageBox
from date.sucursalDate import SucursalDate



class VentanaConsultaPrincipal(QDialog):
    def __init__(self, ventanaMenu):
        super().__init__()
        self.ui = uic.loadUi('ui\consulta_form_principal.ui',self)
        self.ventana_menu= ventanaMenu
        self.ventana_menu.hide()



        #conectamos la UI a las variables de la clase.
        self.c1 = self.ui.radioButtonc1
        self.c2 = self.ui.radioButtonc2
        

        self.result_table = self.ui.tableWidget
        self.result_table.setSortingEnabled(False)
        
        
        # Initialize signal-slot connections
        self.init_signal_slot()
        #intancia que me permite hacer las Querys a Base de Datos
        self.sucursal_date = SucursalDate()
        self.buscar_registro()
        self.ui.show()


    def init_signal_slot(self):
        # Conección de los botones a sus respectivas funciones
        self.generarConsulta_btn.clicked.connect(self.generar_consulta)
        self.back_btn.clicked.connect(self.regresar_atras)
        self.limpiar_btn.clicked.connect(self.limpiar_formulario)
        
        

    def generar_consulta(self):

        if self.c1.isChecked():

            print("presiono el check 1")
            search_result = self.sucursal_date.sucursales_munImportate()
            self.mostrar_info_tabla(search_result)

        if self.c2.isChecked():
            
            search_result = self.sucursal_date.sucursales_munMedellin()
            self.mostrar_info_tabla(search_result)
            print("presiono el check 2")    
        
  
    def limpiar_formulario(self):      
        #se actualiza la tabla
        self.buscar_registro()

    
    def buscar_registro(self):
        
        search_result = self.sucursal_date.buscar_informacion()

        #result = self.empleado_date.consultarEmpleados_tabla()
        self.mostrar_info_tabla(search_result)
   
  
    
    def mostrar_info_tabla(self, result):
        # Function to populate the table with student information
        ## Función para llenar la tabla con información del estudiante
        if result:
            self.result_table.setRowCount(0)
            self.result_table.setRowCount(len(result))

            #saca el indice y la fila de la tabla
            for row, info in enumerate(result):
                

                for column, item in enumerate(info):
                    cell_item = QTableWidgetItem(str(item))
                    self.result_table.setItem(row, column, cell_item)

        else:
            self.result_table.setRowCount(0)
            return

               
            
    def regresar_atras(self):
        from ui.menu import VentanaMenu
        self.ventana_menu.show()
        self.close()
                