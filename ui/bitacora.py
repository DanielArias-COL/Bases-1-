from PyQt6 import uic 

from PyQt6.QtWidgets import QDialog, QTableWidgetItem, QPushButton, QMessageBox
from date.bitacoraUsuarioDate import BitacoraUsuarioDate



class VentanaBitacora(QDialog):
    def __init__(self, ventanaMenu):
        super().__init__()
        self.ui = uic.loadUi('ui/bitacora_usuario_form.ui',self)
        #conectamos la UI a las variables de la clase.
        self.ventana_menu= ventanaMenu
        self.ventana_menu.hide()

        self.bitacora_id = self.ui.lineEditCodigo
        

        self.result_table = self.ui.tableWidget
        self.result_table.setSortingEnabled(False)
        
        
        # Initialize signal-slot connections
        self.init_signal_slot()
        #intancia que me permite hacer las Querys a Base de Datos
        self.bitacora_date = BitacoraUsuarioDate()
        
        self.buscar_registro()
        self.ui.show()


    def init_signal_slot(self):
        # Conección de los botones a sus respectivas funciones
        self.search_btn.clicked.connect(self.buscar_registro)
        self.clear_btn.clicked.connect(self.limpiar_formulario)
        self.back_btn.clicked.connect(self.regresar_atras)
        
        

    def desactivar_botones(self):
        # Desactivar todos los botones
        for button in self.buttons_list:
            button.setDisabled(True)

    def activar_botones(self):
        # Activar todos los botones
        for button in self.buttons_list:
            button.setDisabled(False)    

    
    def buscar_registro(self):
        # Function to search for student information and populate the table
        bitacora_id =  self.bitacora_id.text().strip()
   
        search_result = self.bitacora_date.buscar_informacion(bitacora_id)

        #result = self.empleado_date.consultarEmpleados_tabla()
        self.mostrar_info_tabla(search_result)
   
    def limpiar_formulario(self):
        # Función que limpia el formulario
    
        self.bitacora_id.clear()
        
        
        #se actualiza la tabla
        self.buscar_registro()
        
        
        

    def verificar_bitacora_id(self, id):
        # Función que verifica si un empleado ya existe
        result = self.empleado_date.buscar_empleado(empleado_id=id)
        return result

    
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

    def seleccionar_registro(self):
        select_row = self.result_table.currentRow()
        if select_row != -1:
            self.empleado_id.setEnabled(False)
            
            empleado_id = self.result_table.item(select_row, 0).text().strip()
            cedula = self.result_table.item(select_row, 1).text().strip()
            nombre = self.result_table.item(select_row, 2).text().strip()
            direccion = self.result_table.item(select_row, 4).text().strip()
            telefono = self.result_table.item(select_row, 3).text().strip()
           
            self.empleado_id.setText(empleado_id)
            self.empleado_cedula.setText(cedula)
            self.empleado_nombre.setText(nombre)
            self.empleado_direccion.setText(direccion)
            self.empleado_telefono.setText(telefono)

        else:
            QMessageBox.information(self, "Warning", "Please select one student information",
                                    QMessageBox.StandardButton.Ok)
        
    
            
            
    def regresar_atras(self):
        from ui.menu import VentanaMenu
        self.ventana_menu.show()
        self.close()    