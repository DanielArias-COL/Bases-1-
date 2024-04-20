from PyQt6 import uic 

from PyQt6.QtWidgets import QDialog

from ui.menu import VentanaMenu

class Login(QDialog):
    def __init__(self):
        super().__init__()
        self.login = uic.loadUi('ui\login_form.ui',self)
        self.login.btnIniciarSesion.clicked.connect(self.autenticarUsuario)
        self.login.show()

    def autenticarUsuario(self):
        self.close()
        ventana_menu = VentanaMenu()
      