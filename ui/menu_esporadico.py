from PyQt6 import uic
from PyQt6.QtWidgets import QMainWindow, QMessageBox
from ui.listaSuc import VentanaListaSuc
from ui.reporte import VentanaGestorInformes
from date.bitacoraUsuarioDate import BitacoraUsuarioDate
from ui.consulta_esporadico import VentanaConsultaEsporadico



class VentanaMenuEsporadico(QMainWindow):
    def __init__(self,usuario_id = None, nivel_usuario = None):
        super().__init__()
        self.usuario_id= usuario_id
        self.nivel_usuario = nivel_usuario
        self.ui = uic.loadUi('ui/menu_form_esporadico.ui',self)
        self.initGUI()
        self.bitacora_Date= BitacoraUsuarioDate()
        self.fecha_ingreso = self.bitacora_Date.obtener_fecha()
        self.ui.show()

    def initGUI(self):
        self.ui.btnAbrirbtnAbrirInformes.triggered.connect(lambda: self.ventanaInformes())
        self.ui.btnAbrirConsultas.triggered.connect(lambda: VentanaConsultaEsporadico(self))
        


        self.ui.btnAbrirAyudaApp.triggered.connect(lambda: QMessageBox.information(self, "Ayuda de la aplicación",
            "1. En la primera sección, Entidades, podrás gestionar todos los registros relacionados con las entidades. Aquí tendrás la opción de agregar, eliminar, editar y actualizar cualquier registro, así como buscar información de manera rápida y eficiente.\n"+"\n"+
            "2. En la sección de Transacciones, podrás gestionar todos los contratos y transacciones. Al igual que en la sección de entidades, tendrás la libertad de agregar, eliminar, editar y actualizar cualquier registro, además de la posibilidad de realizar búsquedas personalizadas.\n"+"\n"+
            "3. En la sección de Reportes y Consultas, podrás generar informes en formato PDF sobre las entidades, así como listar y buscar sucursales de forma cómoda y rápida.\n"+"\n"+
            "4. En la sección de Utilidades, podrás gestionar usuarios mediante un conjunto completo de operaciones CRUD (Crear, Leer, Actualizar, Eliminar). Además, tendrás acceso a las bitácoras del sistema, donde podrás revisar las actividades registradas cada vez que un usuario ingresa a la plataforma.\n"+"\n"+
            "Estas secciones están diseñadas para proporcionar una experiencia de usuario intuitiva y eficiente, facilitando la gestión y el seguimiento de la información en nuestra plataforma.",
            QMessageBox.StandardButton.Ok)  )
        

        self.ui.btnAbrirAcercaDe.triggered.connect(lambda: QMessageBox.information(self, "Acerca De",
            "Unibank es una plataforma diseñada para brindarte un control completo sobre tus operaciones financieras."+
            "Con Unibank, puedes gestionar fácilmente todos los aspectos relacionados con tus entidades, transacciones,"+
            "reportes y usuarios.\n"+
            "Estas secciones están diseñadas para ofrecerte una experiencia de usuario intuitiva y eficiente, permitiéndote"+
            "gestionar y dar seguimiento a la información de manera efectiva en nuestra plataforma Unibank.",
            QMessageBox.StandardButton.Ok)  )

        self.btnCerrarSesion.clicked.connect(self.cerrarSesion)


        

          

    def cerrarSesion(self):
        from ui.login import Login
        self.agregar_bitacora(self.fecha_ingreso, self.usuario_id)
        self.close()
        Login()


    def ventanaListaSuc(self):
        self.close()
        VentanaListaSuc(self)

    def ventanaInformes(self):
        self.close()
        VentanaGestorInformes(self, self.nivel_usuario)

    def agregar_bitacora(self, fecha_entrada, usr_id):
        self.bitacora_Date.agregar_bitacora(fecha_entrada=fecha_entrada, usr_id=usr_id)
        

    

    
        


    