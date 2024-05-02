from PyQt6 import uic 

from PyQt6.QtWidgets import QDialog, QTableWidgetItem, QPushButton, QMessageBox
from date.municipioDate import MunicipioDate



class VentanaMunicipio(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = uic.loadUi('ui\municipio_form.ui',self)
        #conectamos la UI a las variables de la clase.
        self.municipio_id = self.ui.lineEditCodigo
        self.municipio_nombre = self.ui.lineEditNombre
        self.municipio_poblacion = self.ui.lineEditPoblacion
        self.municipio_DepartamentoId = self.ui.lineEditDepartamentoId
        self.municipio_PrioridadId = self.ui.lineEditPrioridadId

        self.result_table = self.ui.tableWidget
        self.result_table.setSortingEnabled(False)
        self.buttons_list = self.ui.function_frame.findChildren(QPushButton)
        
        # Initialize signal-slot connections
        self.init_signal_slot()
        #intancia que me permite hacer las Querys a Base de Datos
        self.municipio_date = MunicipioDate()
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

        municipio_info = self.obtener_municipio()

        if municipio_info["Id"] and municipio_info["Nombre"] and municipio_info["Poblacion"] and municipio_info["dep_id"] and municipio_info["prd_id"] :
            check_result = self.verificar_municipio_id(int(municipio_info["Id"]))

            
            if check_result:
                QMessageBox.information(self, "Warning", "Por favor ingrese un nuevo código para el empleado",
                                        QMessageBox.StandardButton.Ok)
                self.activar_botones()
                return
            


            add_result = self.municipio_date.agregar_municipio(int(municipio_info["Id"]),
                                                       municipio_info["Nombre"],
                                                       int(municipio_info["Poblacion"]),
                                                       int(municipio_info["dep_id"]),
                                                       int(municipio_info["prd_id"]))
                                          

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
        municipio_info = self.obtener_municipio()

        search_result = self.municipio_date.buscar_informacion(
            id=municipio_info["Id"],
            nombre=municipio_info["Nombre"],
            poblacion=municipio_info["Poblacion"],
            dep_id=municipio_info["dep_id"],
            prd_id=municipio_info["prd_id"]
        )

        #result = self.empleado_date.consultarEmpleados_tabla()
        self.mostrar_info_tabla(search_result)
   
    def limpiar_formulario(self):
        # Función que limpia el formulario
        self.municipio_id.setEnabled(True)
        self.municipio_id.clear()
        self.municipio_nombre.clear()
        self.municipio_poblacion.clear()
        self.municipio_DepartamentoId.clear()
        self.municipio_PrioridadId.clear()
        #se actualiza la tabla
        self.buscar_registro()
        
        
        

    def verificar_municipio_id(self, id):
        # Función que verifica si un empleado ya existe
        result = self.municipio_date.buscar_municipio(municipio_id=id)
        return result

    def obtener_municipio(self):
        # Funcion que devuelve el empleado del formulario
        municipio_id = self.municipio_id.text().strip()
        nombre = self.municipio_nombre.text().strip()
        poblacion = self.municipio_poblacion.text().strip()
        DepartamentoId = self.municipio_DepartamentoId.text().strip()
        PrioridadId = self.municipio_PrioridadId.text().strip()
        

        municipio_info = {
            "Id": municipio_id,
            "Nombre": nombre,
            "Poblacion": poblacion,
            "dep_id": DepartamentoId,
            "prd_id": PrioridadId,
        }

        return municipio_info
    
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
            self.municipio_id.setEnabled(False)
            
            municipio_id = self.result_table.item(select_row, 0).text().strip()
            nombre = self.result_table.item(select_row, 1).text().strip()
            cantidad_poblacion = self.result_table.item(select_row, 2).text().strip()
            dep_id = self.result_table.item(select_row, 4).text().strip()
            prd_id = self.result_table.item(select_row, 3).text().strip()
           
            self.municipio_id.setText(municipio_id)
            self.municipio_nombre.setText(nombre)
            self.municipio_poblacion.setText(cantidad_poblacion)
            self.municipio_DepartamentoId.setText(dep_id)
            self.municipio_PrioridadId.setText(prd_id)

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
                
                municipio_id = self.result_table.item(select_row, 0).text().strip()
                #se elimina y se actualiza la tabla
                delete_result = self.municipio_date.eliminar_municipio(municipio_id)
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
        new_municipio_info = self.obtener_municipio()

        if new_municipio_info["Id"]:
            update_result = self.municipio_date.actualizar_municipio(
                id=new_municipio_info["Id"],
                nombre=new_municipio_info["Nombre"],
                cantidad_poblacion=new_municipio_info["Poblacion"],
                dep_id=new_municipio_info["dep_id"],
                prd_id=new_municipio_info["prd_id"],
                
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