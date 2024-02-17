import sys
from PyQt5 import uic, QtWidgets
from PyQt5.QtCore import Qt
qtCreatorFile = "E_04_EcuacionPrimerGrado.ui"  # Nombre del archivo aquí.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Configuración de la ventana
        self.setFixedSize(445, 374)  # Establece el tamaño fijo de la ventana
        self.setWindowFlags(self.windowFlags() & ~Qt.WindowMaximizeButtonHint)  # Deshabilita el botón de maximizar
        self.setWindowFlags(self.windowFlags() & ~Qt.WindowMinimizeButtonHint)  # Deshabilita el botón de minimizar

        # Restringe la ventana a no ser redimensionable
        self.setFixedSize(self.size())

        # Área de los Signals
        self.btn_calcular.clicked.connect(self.calcularEc)
        self.txt_result.setEnabled(False)

    # Área de los Slots
    def calcularEc(self):
        m = int(self.txt_m_2.text())
        x = int(self.txt_x_2.text())
        b = int(self.txt_b_2.text())
        result = (m*x) + b
        self.txt_result.setText(str(result))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())