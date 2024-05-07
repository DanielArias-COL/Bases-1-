from PyQt6 import uic 

from PyQt6.QtWidgets import QDialog, QTableWidgetItem, QPushButton, QMessageBox
from date.cargoDate import CargoDate



class VentanaCargo(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = uic.loadUi('ui\cargo_form.ui',self)
        #conectamos la UI a las variables de la clase.
        self.cargo_id = self.ui.lineEditCodigo
        self.cargo_nombre = self.ui.lineEditNombre
        self.cargo_salario = self.ui.lineEditSalario
        
        

        self.result_table = self.ui.tableWidget
        self.result_table.setSortingEnabled(False)
        self.buttons_list = self.ui.function_frame.findChildren(QPushButton)
        
        # Initialize signal-slot connections
        self.init_signal_slot()
        #intancia que me permite hacer las Querys a Base de Datos
        self.cargo_date = CargoDate()
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

        cargo_info = self.obtener_cargo()

        if cargo_info["carg_id"] and cargo_info["nombre"] and cargo_info["salario"]  :
            check_result = self.verificar_cargo_id(int(cargo_info["carg_id"]))

            
            if check_result:
                QMessageBox.information(self, "Warning", "Por favor ingrese un nuevo código para el empleado",
                                        QMessageBox.StandardButton.Ok)
                self.activar_botones()
                return
            
            

            add_result = self.cargo_date.agregar_Cargo(int(cargo_info["carg_id"]),
                                                       cargo_info["nombre"],
                                                       int(cargo_info["salario"]))
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
        cargo_info = self.obtener_cargo()

        search_result = self.cargo_date.buscar_informacion(
            suc_id=cargo_info["carg_id"],
            nombre=cargo_info["nombre"],
            salario=cargo_info["salario"]
        )

        #result = self.empleado_date.consultarEmpleados_tabla()
        self.mostrar_info_tabla(search_result)
   
    def limpiar_formulario(self):
        # Función que limpia el formulario
        self.cargo_id.setEnabled(True)
        self.cargo_id.clear()
        self.cargo_nombre.clear()
        self.cargo_salario.clear()
        
        
        #se actualiza la tabla
        self.buscar_registro()
        
        
        

    def verificar_cargo_id(self, id):
        # Función que verifica si un empleado ya existe
        result = self.cargo_date.buscar_Cargo(cargo_id=id)
        return result

    def obtener_cargo(self):
        # Funcion que devuelve el empleado del formulario
        carg_id = self.cargo_id.text().strip()
        nombre = self.cargo_nombre.text().strip()
        salario = self.cargo_salario.text().strip()
        
        

        cargo_info = {
            "carg_id": carg_id,
            "nombre": nombre,
            "salario": salario
        }

        return cargo_info
    
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
            self.cargo_id.setEnabled(False)
            
            cargo_id = self.result_table.item(select_row, 0).text().strip()
            nombre = self.result_table.item(select_row, 1).text().strip()
            salario = self.result_table.item(select_row, 2).text().strip()
            
           
            self.cargo_id.setText(cargo_id)
            self.cargo_nombre.setText(nombre)
            self.cargo_salario.setText(salario)

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
                
                cargo_id = self.result_table.item(select_row, 0).text().strip()
                #se elimina y se actualiza la tabla
                delete_result = self.cargo_date.eliminar_Cargo(cargo_id)
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
        new_sucursal_info = self.obtener_cargo()

        if new_sucursal_info["carg_id"]:
            update_result = self.cargo_date.actualizar_Cargo(
                carg_id=new_sucursal_info["carg_id"],
                nombre=new_sucursal_info["nombre"],
                salario=new_sucursal_info["salario"]
                
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
        self.close()
        ventana_menu = VentanaMenu()
        pass        