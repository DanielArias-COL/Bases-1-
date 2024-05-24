from PyQt6 import uic 

from PyQt6.QtWidgets import QDialog, QTableWidgetItem, QPushButton, QMessageBox
from date.profesionDate import ProfesionDate



class VentanaProfesion(QDialog):
    def __init__(self, ventanaMenu):
        super().__init__()
        self.ui = uic.loadUi('ui\profesion_form.ui',self)

        self.ventana_menu= ventanaMenu
        self.ventana_menu.hide()

        #conectamos la UI a las variables de la clase.
        self.profesion_id = self.ui.lineEditCodigo
        self.profesion_nombre = self.ui.lineEditNombre
        
        
        

        self.result_table = self.ui.tableWidget
        self.result_table.setSortingEnabled(False)
        self.buttons_list = self.ui.function_frame.findChildren(QPushButton)
        
        # Initialize signal-slot connections
        self.init_signal_slot()
        #intancia que me permite hacer las Querys a Base de Datos
        self.profesion_date = ProfesionDate()
        self.buscar_registro()
        self.ui.show()


    def init_signal_slot(self):
        # Conección de los botones a sus respectivas funciones
        self.add_btn.clicked.connect(self.agregar_registro)
        self.search_btn.clicked.connect(self.buscar_registro)
        self.clear_btn.clicked.connect(self.limpiar_formulario)
        self.select_btn.clicked.connect(self.seleccionar_registro)
        self.update_btn.clicked.connect(self.actualizar_registro)
        self.delete_btn.clicked.connect(self.eliminar_registro)
        self.back_btn.clicked.connect(self.regresar_atras)
        

    def desactivar_botones(self):
        # Desactivar todos los botones
        for button in self.buttons_list:
            button.setDisabled(True)

    def activar_botones(self):
        # Activar todos los botones
        for button in self.buttons_list:
            button.setDisabled(False)    

    def agregar_registro(self):
        # Función que agrega al empleado a la base de datos
        self.desactivar_botones()

        profesion_info = self.obtener_profesion()

        if profesion_info["prf_id"] and profesion_info["nombre"]   :
            check_result = self.verificar_profesion_id(int(profesion_info["prf_id"]))

            
            if check_result:
                QMessageBox.information(self, "Warning", "Por favor ingrese un nuevo código para el empleado",
                                        QMessageBox.StandardButton.Ok)
                self.activar_botones()
                return
            
            

            add_result = self.profesion_date.agregar_profesion(int(profesion_info["prf_id"]),
                                                       profesion_info["nombre"])
            self.limpiar_formulario()         
            self.buscar_registro()

            if add_result:
                QMessageBox.information(self, "Warning", f"Add fail: {add_result}, Please try again.",
                                        QMessageBox.StandardButton.Ok)

        else:
            QMessageBox.information(self, "Warning", "Please input student ID and first name.",
                                    QMessageBox.StandardButton.Ok)

        
        self.activar_botones()

    def buscar_registro(self):
        # Function to search for student information and populate the table
        profesion_info = self.obtener_profesion()

        search_result = self.profesion_date.buscar_informacion(
            prf_id=profesion_info["prf_id"],
            nombre=profesion_info["nombre"]
        )

        #result = self.empleado_date.consultarEmpleados_tabla()
        self.mostrar_info_tabla(search_result)
   
    def limpiar_formulario(self):
        # Función que limpia el formulario
        self.profesion_id.setEnabled(True)
        self.profesion_id.clear()
        self.profesion_nombre.clear()
        
    
        #se actualiza la tabla
        self.buscar_registro()
        
        
        

    def verificar_profesion_id(self, id):
        # Función que verifica si un empleado ya existe
        result = self.profesion_date.buscar_Profesion(profesion_id=id)
        return result

    def obtener_profesion(self):
        # Funcion que devuelve el empleado del formulario
        prf_id = self.profesion_id.text().strip()
        nombre = self.profesion_nombre.text().strip()
        

        profesion_info = {
            "prf_id": prf_id,
            "nombre": nombre
        }

        return profesion_info
    
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
            self.profesion_id.setEnabled(False)
            
            profesion_id = self.result_table.item(select_row, 0).text().strip()
            nombre = self.result_table.item(select_row, 1).text().strip()
            
           
            self.profesion_id.setText(profesion_id)
            self.profesion_nombre.setText(nombre)
            

        else:
            QMessageBox.information(self, "Warning", "Please select one student information",
                                    QMessageBox.StandardButton.Ok)
        
    
    def eliminar_registro(self):
        # Funcion para elimar un empleado
        select_row = self.result_table.currentRow()
        if select_row != -1:
            selected_option = QMessageBox.warning(self, "Warning", "Estas seguro de eliminar el registro?",
                                                  QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.Cancel)

            if selected_option == QMessageBox.StandardButton.Yes:
                
                profesion_id = self.result_table.item(select_row, 0).text().strip()
                #se elimina y se actualiza la tabla
                delete_result = self.profesion_date.eliminar_profesion(profesion_id)
                self.limpiar_formulario()
                self.buscar_registro()
                

                if not delete_result:
                    self.buscar_registro()
                else:
                    QMessageBox.information(self, "Warning",
                                            f"Fail to delete the information: {delete_result}. Please try again.",
                                            QMessageBox.StandardButton.Ok)

        else:
            QMessageBox.information(self, "Warning", "Por favor seleccione un registro primero",
                                    QMessageBox.StandardButton.Ok)    
            
    def actualizar_registro(self):
        # Function to update student information
        new_profesion_info = self.obtener_profesion()

        if new_profesion_info["prf_id"]:
            update_result = self.profesion_date.actualizar_profesion(
                prf_id=new_profesion_info["prf_id"],
                nombre=new_profesion_info["nombre"]
                
            )

            if update_result:
                QMessageBox.information(self, "Warning",
                                        f"Error al actualizar la información: {update_result}. Por favor intentelo de nuevo.",
                                        QMessageBox.StandardButton.Ok)
            else:
                self.limpiar_formulario()
                self.buscar_registro()
        else:
            QMessageBox.information(self, "Warning",
                                    f"Por favor selecione un empleado primero .",
                                    QMessageBox.StandardButton.Ok)        
            
    def regresar_atras(self):
        from ui.menu import VentanaMenu
        self.ventana_menu.show()
        self.close()   