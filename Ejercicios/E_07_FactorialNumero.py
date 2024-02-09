import sys
from PyQt5 import uic, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMessageBox

qtCreatorFile = "E_07_FactorialNumero.ui"
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Configuración de la ventana
        self.setFixedSize(385, 348)  # Establece el tamaño fijo de la ventana
        self.setWindowFlags(self.windowFlags() & ~Qt.WindowMaximizeButtonHint)  # Deshabilita el botón de maximizar
        self.setWindowFlags(self.windowFlags() & ~Qt.WindowMinimizeButtonHint)  # Deshabilita el botón de minimizar

        # Restringe la ventana a no ser redimensionable
        self.setFixedSize(self.size())

        # Área de los Signals
        self.btn_calcular.clicked.connect(self.calcular_factorial)
        self.txt_result.setEnabled(False)


    # Área de los Slots
    def calcular_factorial(self):
        try:
            numero = int(self.txt_factorial.text())
            if numero < 0:
                raise ValueError("El número debe ser un entero positivo.")
            else:
                resultado = self.factorial(numero)
                self.txt_result.setText(str(resultado))

        except ValueError as error:
            QMessageBox.warning(self, "Error", str(error))

    def factorial(self, n):
        resultado = 1
        for i in range(1, n + 1):
            resultado *= i
        return resultado

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
