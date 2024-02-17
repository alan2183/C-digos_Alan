import sys
from PyQt5 import uic, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMessageBox

qtCreatorFile = "E_01_CalcularAreaRectangulo.ui"  # Nombre del archivo aquí.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Configuración general de la ventana
        self.setFixedSize(518, 299)  # Establecer el tamaño fijo de la ventana
        self.setWindowFlags(self.windowFlags() & ~Qt.WindowMaximizeButtonHint)  # se deshabilita el botón de maximizar
        self.setWindowFlags(self.windowFlags() & ~Qt.WindowMinimizeButtonHint)  # se deshabilita el botón de minimizar

        # se restringe la ventana a no ser redimensionable
        self.setFixedSize(self.size())
    
        # Área de los Signals
        self.btn_calcular.clicked.connect(self.calcular)
        self.txt_result.setEnabled(False)

    # Área de los Slots
    def calcular(self):
        try:
            longitud = float(self.txt1.text())
            ancho = float(self.txt2.text())
            if longitud <= 0 or ancho <= 0:
                raise ValueError("Tanto la longitud como el ancho deben ser mayores que cero")
            area = longitud*ancho
            self.txt_result.setText(str(area))

        except ValueError as error:
            QMessageBox.warning(self, "Error", str(error))

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
