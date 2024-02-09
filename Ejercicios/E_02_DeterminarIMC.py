import sys
from PyQt5.QtCore import Qt
from PyQt5 import uic, QtWidgets
from PyQt5.QtWidgets import QMessageBox

qtCreatorFile = "E_02_DeterminarIMC.ui"
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Configuración de la ventana
        self.setFixedSize(583, 329)  # Establece el tamaño fijo de la ventana
        self.setWindowFlags(self.windowFlags() & ~Qt.WindowMaximizeButtonHint)  # Deshabilita el botón de maximizar
        self.setWindowFlags(self.windowFlags() & ~Qt.WindowMinimizeButtonHint)  # Deshabilita el botón de minimizar

        # Restringe la ventana a no ser redimensionable
        self.setFixedSize(self.size())

        # Área de los Signals
        self.btn_IMC.clicked.connect(self.calcularIMC)
        self.txt_result.setEnabled(False)

    # Área de los Slots
    def calcularIMC(self):
        try:
            peso = float(self.txt_peso.text())
            altura = float(self.txt_altura.text())

            # Validar que la altura sea un número decimal positivo
            if altura > 3.0:  # Puedes ajustar el rango según tus necesidades
                raise ValueError("La altura debe ser mayor a cero y con decimales")

            IMC = peso / (altura * altura)
            IMCredondeado = round(IMC, 2)

            self.txt_result.setText(str(IMCredondeado))

        except ValueError as error:
            QMessageBox.warning(self, "Error", str(error))

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
