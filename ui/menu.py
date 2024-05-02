from PyQt6 import uic
from PyQt6.QtWidgets import QMainWindow
from ui.empleado import VentanaEmpleado
from ui.departamento import VentanaDepartamento
from ui.municipio import VentanaMunicipio

class VentanaMenu(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = uic.loadUi('ui/menu_form.ui',self)
        self.initGUI()
        self.ui.show()

    def initGUI(self):
        self.ui.btnAbrirVentanaEmpleado.triggered.connect(lambda: VentanaEmpleado())
        self.ui.btnAbrirVentanaDepartamento.triggered.connect(lambda: VentanaDepartamento())
        self.ui.btnAbrirVentanaMunicipio.triggered.connect(lambda: VentanaMunicipio())
