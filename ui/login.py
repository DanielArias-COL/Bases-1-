from PyQt6 import uic 

from PyQt6.QtWidgets import QDialog

from ui.menu import VentanaMenu
from ui.menu_parametrico import VentanaMenuParametrico
from ui.menu_esporadico import VentanaMenuEsporadico
from date.loginDate import LoginDate
from date.usuarioDate import UsuarioDate

class Login(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = uic.loadUi('ui\login_form.ui',self)
        self.usuario = self.ui.lineEditUsuario
        self.clave = self.ui.lineEditClave
        self.error_mesage = self.ui.labelError
        self.error_mesage.setText("")
        self.login_date = LoginDate()
        self.usuario_date = UsuarioDate()
        self.init_signal_slot()
        self.ui.show()

        
        

        
    def init_signal_slot(self):
        self.ui.btnIniciarSesion.clicked.connect(self.autenticarUsuario)
        

    def autenticarUsuario(self):
        usuario = self.usuario.text().strip()
        clave = self.clave.text().strip()
        
        resultado = self.login_date.validar_usuario(usuario, clave)

        if resultado:
            self.close()
            user = self.usuario_date.obtener_usuario_nombre(usuario)
            codigo_usuario = user[0][0]
            nivel_usuario = user[0][3]

            if nivel_usuario == "Principal":
                VentanaMenu(usuario_id=codigo_usuario, nivel_usuario= nivel_usuario)

            if nivel_usuario == "Paramétrico":
                VentanaMenuParametrico(usuario_id=codigo_usuario, nivel_usuario= nivel_usuario)

            if nivel_usuario == "Esporádico":
                VentanaMenuEsporadico(usuario_id=codigo_usuario, nivel_usuario= nivel_usuario)

                
        else:
            self.error_mesage.setText("usuario o clave no valida") 

    def iniciar_sin_autenticar(self):
        VentanaMenuEsporadico(usuario_id=902 , nivel_usuario = "Esporádico") 
        self.close()          


        

    
      