import sys
from PyQt5 import uic, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMessageBox

qtCreatorFile = "E_08_DeterminarNota.ui"  # Nombre del archivo aquí.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Configuración general de la ventana
        self.setFixedSize(500, 242)  # Establecer el tamaño fijo de la ventana
        self.setWindowFlags(self.windowFlags() & ~Qt.WindowMaximizeButtonHint)  # Deshabilita el botón de maximizar
        self.setWindowFlags(self.windowFlags() & ~Qt.WindowMinimizeButtonHint)  # Deshabilita el botón de minimizar

        # Restringe la ventana a no ser redimensionable
        self.setFixedSize(self.size())

        # Área de los Signals
        self.btn_calcularNota.clicked.connect(self.calcular)
        self.txt_result.setEnabled(False)

    # Área de los Slots
    def calcular(self):
        alumno = self.txt_nombre.text()
        calificacion_str = self.txt_calif.text()

        try:
            calificacion = int(calificacion_str)
            if calificacion < 0 or calificacion > 10:
                raise ValueError("La calificación debe estar entre 0 y 10")

            if calificacion == 10:
                nota = "A"
            elif calificacion == 9:
                nota = "B"
            elif calificacion == 8:
                nota = "C"
            elif calificacion == 7:
                nota = "D"
            elif calificacion == 6:
                nota = "E"
            else:
                nota = "F"

            cadena = "La nota de " + alumno + " es " + nota
            self.txt_result.setText(cadena)

        except ValueError as error:
            QMessageBox.warning(self, "Error", str(error))

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())

