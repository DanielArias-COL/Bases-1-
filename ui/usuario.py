from PyQt6 import uic 

from PyQt6.QtWidgets import QDialog, QTableWidgetItem, QPushButton, QMessageBox
from date.usuarioDate import UsuarioDate



class VentanaUsuario(QDialog):
    def __init__(self, ventanaMenu):
        super().__init__()
        self.ui = uic.loadUi('ui/usuario_form.ui',self)
        #conectamos la UI a las variables de la clase.
        self.ventana_menu= ventanaMenu
        self.ventana_menu.hide()


        self.usuario_codigoEmp = self.ui.lineEditCodigoEmpleado
        self.usuario_nombreAlt = self.ui.lineEditNombreAlt
        self.usuario_clave = self.ui.lineEditClave
        self.usuario_nivel = self.ui.comboBoxNivelUsuario
        

        self.result_table = self.ui.tableWidget
        self.result_table.setSortingEnabled(False)
        self.buttons_list = self.ui.function_frame.findChildren(QPushButton)
        
        # Initialize signal-slot connections
        self.init_signal_slot()
        #intancia que me permite hacer las Querys a Base de Datos
        self.usuario_date = UsuarioDate()
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

        usuario_info = self.obtener_usuario()

        if usuario_info["usr_id"] and usuario_info["nombre_alternativo"] and usuario_info["clave"] and usuario_info["nivel_usuario"] :
            check_result = self.verificar_usuario_id(int(usuario_info["usr_id"]))

            
            if check_result:
                QMessageBox.information(self, "Warning", "Por favor ingrese un nuevo código para el usuario",
                                        QMessageBox.StandardButton.Ok)
                self.activar_botones()
                return
            
            

            add_result = self.usuario_date.agregar_usuario(int(usuario_info["usr_id"]),
                                                       usuario_info["nombre_alternativo"],
                                                       int(usuario_info["clave"]),
                                                       usuario_info["nivel_usuario"])
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
        empleado_info = self.obtener_usuario()

        search_result = self.usuario_date.buscar_informacion(
            usr_id=empleado_info["usr_id"],
            nombre_alternativo=empleado_info["nombre_alternativo"],
            clave=empleado_info["clave"],
            nivel_usuario=empleado_info["nivel_usuario"]
        )

        #result = self.empleado_date.consultarEmpleados_tabla()
        self.mostrar_info_tabla(search_result)
   
    def limpiar_formulario(self):
        # Función que limpia el formulario
        self.usuario_codigoEmp.setEnabled(True)
        self.usuario_codigoEmp.clear()
        self.usuario_nombreAlt.clear()
        self.usuario_clave.clear()
        self.usuario_nivel.setCurrentIndex(0)
        
        
        #se actualiza la tabla
        self.buscar_registro()
        
        
        

    def verificar_usuario_id(self, id):
        # Función que verifica si un empleado ya existe
        result = self.usuario_date.buscar_usuario(usuario_id=id)
        return result

    def obtener_usuario(self):
        # Funcion que devuelve el empleado del formulario
        codigo = self.usuario_codigoEmp.text().strip()
        nombreAlt = self.usuario_nombreAlt.text().strip()
        clave = self.usuario_clave.text().strip()
        nivel = self.usuario_nivel.currentText()
        

        usuario_info = {
            "usr_id": codigo,
            "nombre_alternativo": nombreAlt,
            "clave": clave,
            "nivel_usuario": nivel
        }

        return usuario_info
    
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

            self.usuario_codigoEmp.setEnabled(False)
            codigo = self.result_table.item(select_row, 0).text().strip()
            nombre = self.result_table.item(select_row, 1).text().strip()
            clave = self.result_table.item(select_row, 2).text().strip()
            nivel = self.result_table.item(select_row, 3).text().strip()
           
            print(nivel)
            self.usuario_codigoEmp.setText(codigo)
            self.usuario_nombreAlt.setText(nombre)
            self.usuario_clave.setText(clave)
            
            if nivel == "Principal":
                self.usuario_nivel.setCurrentIndex(1)
            if nivel == "Paramétrico":
                self.usuario_nivel.setCurrentIndex(2)
            if nivel == "Esporádico":
                self.usuario_nivel.setCurrentIndex(3)


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
                
                usuario_id = self.result_table.item(select_row, 0).text().strip()
                #se elimina y se actualiza la tabla
                delete_result = self.usuario_date.eliminar_usuario(usuario_id)
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
        new_usuario_info = self.obtener_usuario()

        if new_usuario_info["usr_id"]:
            update_result = self.usuario_date.actualizar_usuario(
                usr_id=new_usuario_info["usr_id"],
                nombre_alternativo=new_usuario_info["nombre_alternativo"],
                clave=new_usuario_info["clave"],
                nivel_usuario=new_usuario_info["nivel_usuario"]
                
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