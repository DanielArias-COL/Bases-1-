from PyQt6 import uic 

from PyQt6.QtWidgets import QDialog, QTableWidgetItem, QPushButton, QMessageBox
from date.contratoDate import ContratoDate



class VentanaContrato(QDialog):
    def __init__(self, ventanaMenu):
        super().__init__()
        self.ui = uic.loadUi('ui\contrato_form.ui',self)
        self.ventana_menu= ventanaMenu
        self.ventana_menu.hide()

        #conectamos la UI a las variables de la clase.
        self.contrato_id = self.ui.lineEditCodigo
        self.contrato_fecha_inicio = self.ui.lineEditFechaInicio
        self.contrato_fecha_fin = self.ui.lineEditFechaFin
        self.contrato_empleadoID = self.ui.lineEditEmpleadoId
        self.contrato_sucursalID = self.ui.lineEditSucursalId
        self.contrato_cargoID = self.ui.lineEditCargoId


        self.result_table = self.ui.tableWidget
        self.result_table.setSortingEnabled(False)
        self.buttons_list = self.ui.function_frame.findChildren(QPushButton)
        
        # Initialize signal-slot connections
        self.init_signal_slot()
        #intancia que me permite hacer las Querys a Base de Datos
        self.contrato_date = ContratoDate()
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

        contrato_info = self.obtener_contrato()

        if contrato_info["contr_id"] and contrato_info["fecha_inicio"] and contrato_info["fecha_fin"] and contrato_info["emp_id"] and contrato_info["suc_id"] and contrato_info["carg_id"] :
            check_result = self.verificar_contrato_id(int(contrato_info["contr_id"]))

            
            if check_result:
                QMessageBox.information(self, "Warning", "Por favor ingrese un nuevo código para el empleado",
                                        QMessageBox.StandardButton.Ok)
                self.activar_botones()
                return
            
            

            add_result = self.contrato_date.agregar_contrato(int(contrato_info["contr_id"]),
                                                       contrato_info["fecha_inicio"],
                                                       contrato_info["fecha_fin"],
                                                       int(contrato_info["emp_id"]),
                                                       int(contrato_info["suc_id"]),
                                                       int(contrato_info["carg_id"]))
                                          
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
        contrato_info = self.obtener_contrato()

        search_result = self.contrato_date.buscar_informacion(
            contr_id=contrato_info["contr_id"],
            fecha_inicio=contrato_info["fecha_inicio"],
            fecha_fin=contrato_info["fecha_fin"],
            emp_id=contrato_info["emp_id"],
            suc_id=contrato_info["suc_id"],
            carg_id=contrato_info["carg_id"]
        )

        #result = self.empleado_date.consultarEmpleados_tabla()
        self.mostrar_info_tabla(search_result)
   
    def limpiar_formulario(self):
        # Función que limpia el formulario
        self.contrato_id.setEnabled(True)
        self.contrato_id.clear()
        self.contrato_fecha_inicio.clear()
        self.contrato_fecha_fin.clear()
        self.contrato_empleadoID.clear()
        self.contrato_sucursalID.clear()
        self.contrato_cargoID.clear()

        #se actualiza la tabla
        self.buscar_registro()
        
        
        

    def verificar_contrato_id(self, id):
        # Función que verifica si un empleado ya existe
        result = self.contrato_date.buscar_contrato(contrato_id=id)
        return result

    def obtener_contrato(self):
        # Funcion que devuelve el empleado del formulario
        contr_id = self.contrato_id.text().strip()
        fecha_inicio = self.contrato_fecha_inicio.text().strip()
        fecha_fin = self.contrato_fecha_fin.text().strip()
        emp_id = self.contrato_empleadoID.text().strip()
        suc_id = self.contrato_sucursalID.text().strip()
        carg_id = self.contrato_cargoID.text().strip()
        
        

        contrato_info = {
            "contr_id": contr_id,
            "fecha_inicio": fecha_inicio,
            "fecha_fin": fecha_fin,
            "emp_id": emp_id,
            "suc_id": suc_id,
            "carg_id": carg_id,
            
        }

        return contrato_info
    
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
            self.contrato_id.setEnabled(False)
            
            empleado_id = self.result_table.item(select_row, 0).text().strip()
            fecha_inicio = self.result_table.item(select_row, 1).text().strip()
            fecha_fin = self.result_table.item(select_row, 2).text().strip()
            emp_id = self.result_table.item(select_row, 3).text().strip()
            suc_id = self.result_table.item(select_row, 4).text().strip()
            carg_id = self.result_table.item(select_row, 5).text().strip()
           

            self.contrato_id.setText(empleado_id)
            self.contrato_fecha_inicio.setText(fecha_inicio)
            self.contrato_fecha_fin.setText(fecha_fin)
            self.contrato_empleadoID.setText(emp_id)
            self.contrato_sucursalID.setText(suc_id)
            self.contrato_cargoID.setText(carg_id)
    
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
                
                contrato_id = self.result_table.item(select_row, 0).text().strip()
                #se elimina y se actualiza la tabla
                delete_result = self.contrato_date.eliminar_contrato(contrato_id)
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
        new_contrato_info = self.obtener_contrato()

        if new_contrato_info["contr_id"]:
            update_result = self.contrato_date.actualizar_contrato(
                contr_id=new_contrato_info["contr_id"],
                fecha_inicio=new_contrato_info["fecha_inicio"],
                fecha_fin=new_contrato_info["fecha_fin"],
                emp_id=new_contrato_info["emp_id"],
                suc_id=new_contrato_info["suc_id"],
                carg_id=new_contrato_info["carg_id"],
                
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