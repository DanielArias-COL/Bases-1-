from PyQt6 import uic 

from PyQt6.QtWidgets import QDialog, QTableWidgetItem, QPushButton, QMessageBox

from date.empleadoDate import EmpleadoDate


class VentanaEmpleado(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = uic.loadUi('ui\empleado_form.ui',self)
        

        # Connect UI elements to class variables
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
        
        self.empleado_date = EmpleadoDate()
        result = self.empleado_date.consultarEmpleados_tabla()
        self.show_data(result)
        self.ui.show()


    def init_signal_slot(self):
        # Connect buttons to their respective functions
        self.add_btn.clicked.connect(self.add_info)
        self.search_btn.clicked.connect(self.search_info)
        self.clear_btn.clicked.connect(self.clear_form_info)
        #self.select_btn.clicked.connect(self.select_info)
        #self.update_btn.clicked.connect(self.update_info)
        #self.delete_btn.clicked.connect(self.delete_info)

    def disable_buttons(self):
        # Disable all buttons
        for button in self.buttons_list:
            button.setDisabled(True)

    def enable_buttons(self):
        # Enable all buttons
        for button in self.buttons_list:
            button.setDisabled(False)    

    def add_info(self):
        # Function to add student information
        self.disable_buttons()

        student_info = self.get_empleado_info()

        if student_info["Codigo"] and student_info["Cedula"] and student_info["Nombre"] and student_info["Telefono"] :
            check_result = self.check_empleado_id(int(student_info["Codigo"]))

            
            if check_result:
                QMessageBox.information(self, "Warning", "Por favor ingrese un nuevo código para el empleado",
                                        QMessageBox.StandardButton.Ok)
                self.enable_buttons()
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

        self.search_info()
        self.enable_buttons()

    def search_info(self):
        # Function to search for student information and populate the table
        result = self.empleado_date.consultarEmpleados_tabla()
        self.show_data(result)
   
    def clear_form_info(self):
        # Function to clear the form
        self.empleado_id.clear()
        self.empleado_cedula.clear()
        self.empleado_nombre.clear()
        self.empleado_direccion.clear()
        self.empleado_telefono.clear()
        
        

    def check_empleado_id(self, id):
        # Function to check if a student ID already exists
        result = self.empleado_date.buscar_empleado(empleado_id=id)
        return result

    def get_empleado_info(self):
        # Function to retrieve student information from the form
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
    
    def show_data(self, result):
        # Function to populate the table with student information
        ## Función para llenar la tabla con información del estudiante
        if result:
            self.result_table.setRowCount(0)
            self.result_table.setRowCount(len(result))

            #saca el indice y la fila de la tabla
            for row, info in enumerate(result):
                
                info_list = [
                    info["Codigo"],
                    info["Cedula"],
                    info["Nombre"],
                    info["Direccion"],
                    info["Telefono"],
                ]

                for column, item in enumerate(info_list):
                    cell_item = QTableWidgetItem(str(item))
                    self.result_table.setItem(row, column, cell_item)

        else:
            self.result_table.setRowCount(0)
            return

