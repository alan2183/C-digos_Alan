import sys
from PyQt5 import uic, QtWidgets
from PyQt5.QtCore import Qt


qtCreatorFile = "E_05_CalcularPuntoMedio.ui"  # Nombre del archivo aquí.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Configuración de la ventana
        self.setFixedSize(524, 468)  # Establece el tamaño fijo de la ventana
        self.setWindowFlags(self.windowFlags() & ~Qt.WindowMaximizeButtonHint)  # Deshabilita el botón de maximizar
        self.setWindowFlags(self.windowFlags() & ~Qt.WindowMinimizeButtonHint)  # Deshabilita el botón de minimizar

        # Restringe la ventana a no ser redimensionable
        self.setFixedSize(self.size())

        # Área de los Signals
        self.btn_calcular.clicked.connect(self.calcularEc)
        self.txt_result.setEnabled(False)

    # Área de los Slots
    def calcularEc(self):
        x1 = float(self.txt_x1.text())
        y1 = float(self.txt_y1.text())
        x2 = float(self.txt_x2.text())
        y2 = float(self.txt_y2.text())

        punto_medio_x = (x1 + x2) / 2
        punto_medio_y = (y1 + y2) / 2

        cadena = ("El punto medio entre: "+"("+str(x1)+","+str(y1)+") y ("+str(x2)+","+str(y2)+") es: ("+str(punto_medio_x)+","+str(punto_medio_y)+")")
        self.txt_result.setText(cadena)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())