from PyQt6 import uic 

from PyQt6.QtWidgets import QDialog, QTableWidgetItem, QPushButton, QMessageBox
from date.empleadoDate import EmpleadoDate



class VentanaEmpleado(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = uic.loadUi('ui\empleado_form.ui',self)
        #conectamos la UI a las variables de la clase.
        self.empleado_id = self.ui.lineEditCodigo
        self.empleado_cedula = self.ui.lineEditCedula
        self.empleado_nombre = self.ui.lineEditNombre
        self.empleado_direccion = self.ui.lineEditDireccion
        self.empleado_telefono = self.ui.lineEditTelefono

        self.result_table = self.ui.tableWidget
        self.result_table.setSortingEnabled(False)
        self.buttons_list = self.ui.function_frame.findChildren(QPushButton)
        
        # Initialize signal-slot connections
        self.init_signal_slot()
        #intancia que me permite hacer las Querys a Base de Datos
        self.empleado_date = EmpleadoDate()
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

        student_info = self.obtener_empleado()

        if student_info["Codigo"] and student_info["Cedula"] and student_info["Nombre"] and student_info["Telefono"] :
            check_result = self.verificar_empleado_id(int(student_info["Codigo"]))

            
            if check_result:
                QMessageBox.information(self, "Warning", "Por favor ingrese un nuevo código para el empleado",
                                        QMessageBox.StandardButton.Ok)
                self.activar_botones()
                return
            
            print(student_info["Telefono"]+"telefonoooo")

            add_result = self.empleado_date.agregar_empleado(int(student_info["Codigo"]),
                                                       int(student_info["Cedula"]),
                                                       student_info["Nombre"],
                                                       student_info["Direccion"],
                                                       int(student_info["Telefono"]))
                                          

            if add_result:
                QMessageBox.information(self, "Warning", f"Add fail: {add_result}, Please try again.",
                                        QMessageBox.StandardButton.Ok)

        else:
            QMessageBox.information(self, "Warning", "Please input student ID and first name.",
                                    QMessageBox.StandardButton.Ok)

        self.buscar_registro()
        self.activar_botones()

    def buscar_registro(self):
        # Function to search for student information and populate the table
        empleado_info = self.obtener_empleado()

        search_result = self.empleado_date.buscar_informacion(
            id=empleado_info["Codigo"],
            cedula=empleado_info["Cedula"],
            nombre=empleado_info["Nombre"],
            direccion=empleado_info["Direccion"],
            telefono=empleado_info["Telefono"]
        )

        #result = self.empleado_date.consultarEmpleados_tabla()
        self.mostrar_info_tabla(search_result)
   
    def limpiar_formulario(self):
        # Función que limpia el formulario
        self.empleado_id.setEnabled(True)
        self.empleado_id.clear()
        self.empleado_cedula.clear()
        self.empleado_nombre.clear()
        self.empleado_direccion.clear()
        self.empleado_telefono.clear()
        #se actualiza la tabla
        self.buscar_registro()
        
        
        

    def verificar_empleado_id(self, id):
        # Función que verifica si un empleado ya existe
        result = self.empleado_date.buscar_empleado(empleado_id=id)
        return result

    def obtener_empleado(self):
        # Funcion que devuelve el empleado del formulario
        empleado_id = self.empleado_id.text().strip()
        cedula = self.empleado_cedula.text().strip()
        nombre = self.empleado_nombre.text().strip()
        direccion = self.empleado_direccion.text().strip()
        telefono = self.empleado_telefono.text().strip()
        

        student_info = {
            "Codigo": empleado_id,
            "Cedula": cedula,
            "Nombre": nombre,
            "Direccion": direccion,
            "Telefono": telefono,
        }

        return student_info
    
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
                delete_result = self.empleado_date.eliminar_empleado(empleado_id)
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
        new_empleado_info = self.obtener_empleado()

        if new_empleado_info["Codigo"]:
            update_result = self.empleado_date.actualizar_empleado(
                id=new_empleado_info["Codigo"],
                cedula=new_empleado_info["Cedula"],
                nombre=new_empleado_info["Nombre"],
                direccion=new_empleado_info["Direccion"],
                telefono=new_empleado_info["Telefono"],
                
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
        self.close()
        ventana_menu = VentanaMenu()
        pass        