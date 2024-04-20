import sys
from PyQt6.QtWidgets import QApplication, QWidget, QMainWindow, QDialog, QFrame
from PyQt6 import uic
from ui.login_form import Ui_login_form

class Login(QDialog):
    def __init__(self):
        super().__init__()
        #cuando usamos uic, la interfaz se inicializa
        self.ui = uic.loadUi('ui\login_form.ui',self)
        #self.ui = Ui_login_form()
        #self.ui.setupUi(self)  # Inicializa la interfaz de usuario utilizando el método generado por Qt Designer
        self.ui.btnIniciarSesion.clicked.connect(self.autenticarUsuario)
        
        self.show()

    def autenticarUsuario(self):
        self.close()
        ventana_menu = Ventana_menu()
        ventana_menu.show()
   
        
        
        


class Ventana_menu(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = uic.loadUi('ui/menu_form.ui',self)
        #self.ui.BtnSeleccionar.clicked.connect(self.cambiarEntidad)
        
        

    def cambiarEntidad(self):
        print("funciona")
        frameCambio = self.groupBoxDetalleEntidad.findChild(QFrame, "frameCambio")
        nuevoFrame = Ventana_usuarioDetail()
        if frameCambio is not None:
            frameCambio.setLayout(nuevoFrame.layout())
        else:
            print("El frameCambio no se encontró o es None.")



        
class Ventana_usuarioDetail(QFrame):
    def __init__(self):
        super().__init__()
        self.ui = uic.loadUi('ui/usuarioDetail_form.ui',self)
        

if __name__ == '__main__':
    app = QApplication(sys.argv)
    login_window = Login()
    sys.exit(app.exec())
