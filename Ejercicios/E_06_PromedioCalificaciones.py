import sys
from PyQt5 import uic, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5 import QtGui

qtCreatorFile = "E_06_PromedioCalificaciones.ui"  # Nombre del archivo aquí.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Configuración de la ventana
        self.setFixedSize(751, 570)  # Establece el tamaño fijo de la ventana
        self.setWindowFlags(self.windowFlags() & ~Qt.WindowMaximizeButtonHint)  # Deshabilita el botón de maximizar
        self.setWindowFlags(self.windowFlags() & ~Qt.WindowMinimizeButtonHint)  # Deshabilita el botón de minimizar

        # Restringe la ventana a no ser redimensionable
        self.setFixedSize(self.size())

        # Área de los Signals
        self.btn_promedio.clicked.connect(self.calcularPromedio)
        self.txt_result.setEnabled(False)


    # Área de los Slots
    def calcularPromedio(self):
        try:
            calif1 = float(self.txt_c1.text())
            calif2 = float(self.txt_c2.text())
            calif3 = float(self.txt_c3.text())
            calif4 = float(self.txt_c4.text())
            calif5 = float(self.txt_c5.text())

            # Paara verificar si las calificaciones están dentro del rango permitido (0-10)
            if any(calif < 0 or calif > 10 for calif in [calif1, calif2, calif3, calif4, calif5]):
                raise ValueError("Las calificaciones deben estar entre 0 y 10.")

            prom = (calif1 + calif2 + calif3 + calif4 + calif5) / 5
            self.txt_result.setText(str(prom))

        except ValueError as e:
            QtWidgets.QMessageBox.warning(self, "Error", str(e))

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
