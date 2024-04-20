from PyQt6 import uic 

from PyQt6.QtWidgets import QDialog


class VentanaEmpleado(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = uic.loadUi('ui\empleado_form.ui',self)
        self.ui.show()

