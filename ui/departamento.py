from PyQt6 import uic 

from PyQt6.QtWidgets import QDialog, QTableWidgetItem, QPushButton, QMessageBox
from date.departamentoDate import DepartamentoDate



class VentanaDepartamento(QDialog):
    def __init__(self, ventanaMenu):
        super().__init__()
        self.ui = uic.loadUi('ui\departamento_form.ui',self)
        self.ventana_menu= ventanaMenu
        self.ventana_menu.hide()


        #conectamos la UI a las variables de la clase.
        self.departamento_id = self.ui.lineEditCodigo
        self.departamento_nombre = self.ui.lineEditNombre
        self.departamento_poblacion = self.ui.lineEditPoblacion
        

        self.result_table = self.ui.tableWidget
        self.result_table.setSortingEnabled(False)
        self.buttons_list = self.ui.function_frame.findChildren(QPushButton)
        
        # Initialize signal-slot connections
        self.init_signal_slot()
        #intancia que me permite hacer las Querys a Base de Datos
        self.departamento_date = DepartamentoDate()
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

        departamento_info = self.obtener_departamento()

        if departamento_info["Id"] and departamento_info["Nombre"] and departamento_info["Poblacion"]  :
            check_result = self.verificar_departamento_id(int(departamento_info["Id"]))

            
            if check_result:
                QMessageBox.information(self, "Warning", "Por favor ingrese un nuevo código para el empleado",
                                        QMessageBox.StandardButton.Ok)
                self.activar_botones()
                return
            
            

            add_result = self.departamento_date.agregar_departamento(int(departamento_info["Id"]),
                                                                      departamento_info["Nombre"],
                                                                      int(departamento_info["Poblacion"]))
                                                       
                                          

            if add_result:
                QMessageBox.information(self, "Warning", f"Add fail: {add_result}, Please try again.",
                                        QMessageBox.StandardButton.Ok)

        else:
            QMessageBox.information(self, "Warning", "Please input student ID and first name.",
                                    QMessageBox.StandardButton.Ok)

        self.limpiar_formulario()
        self.buscar_registro()
        self.activar_botones()

    def buscar_registro(self):
        # Function to search for student information and populate the table
        departamento_info = self.obtener_departamento()

        search_result = self.departamento_date.buscar_informacion(
            id=departamento_info["Id"],
            nombre=departamento_info["Nombre"],
            poblacion=departamento_info["Poblacion"]
        )

        #result = self.empleado_date.consultarEmpleados_tabla()
        self.mostrar_info_tabla(search_result)
   
    def limpiar_formulario(self):
        # Función que limpia el formulario
        self.departamento_id.setEnabled(True)
        self.departamento_id.clear()
        self.departamento_nombre.clear()
        self.departamento_poblacion.clear()
        #se actualiza la tabla
        self.buscar_registro()
        
        
        

    def verificar_departamento_id(self, id):
        # Función que verifica si un empleado ya existe
        result = self.departamento_date.buscar_departamento(departamento_id=id)
        return result

    def obtener_departamento(self):
        # Funcion que devuelve el empleado del formulario
        departamento_id = self.departamento_id.text().strip()
        nombre = self.departamento_nombre.text().strip()
        poblacion = self.departamento_poblacion.text().strip()
        
        

        departamento_info = {
            "Id": departamento_id,
            "Nombre": nombre,
            "Poblacion": poblacion
        }

        return departamento_info
    
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
            self.departamento_id.setEnabled(False)
            
            empleado_id = self.result_table.item(select_row, 0).text().strip()
            cedula = self.result_table.item(select_row, 1).text().strip()
            nombre = self.result_table.item(select_row, 2).text().strip()
           
            self.departamento_id.setText(empleado_id)
            self.departamento_nombre.setText(cedula)
            self.departamento_poblacion.setText(nombre)
           

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
                print("entroo a el siii")
                empleado_id = self.result_table.item(select_row, 0).text().strip()
                #se elimina y se actualiza la tabla
                delete_result = self.departamento_date.eliminar_departamento(empleado_id)
                

                if not delete_result:
                    self.limpiar_formulario()
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
        new_empleado_info = self.obtener_departamento()

        if new_empleado_info["Id"]:
            update_result = self.departamento_date.actualizar_departamento(
                id=new_empleado_info["Id"],
                nombre=new_empleado_info["Nombre"],
                poblacion=new_empleado_info["Poblacion"]
               
                
            )

            if update_result:
                QMessageBox.information(self, "Warning",
                                        f"Error al actualizar la información: {update_result}. Por favor intentelo de nuevo.",
                                        QMessageBox.StandardButton.Ok)
            else:
                self.buscar_registro()
        else:
            QMessageBox.information(self, "Warning",
                                    f"Por favor selecione un empleado primero .",
                                    QMessageBox.StandardButton.Ok)        
            
    def regresar_atras(self):
        from ui.menu import VentanaMenu
        self.ventana_menu.show()
        self.close()
        
          