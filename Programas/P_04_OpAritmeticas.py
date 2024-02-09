import sys
from PyQt5 import uic, QtWidgets
qtCreatorFile = "P_04_OpMatematicas.ui"  # Nombre del archivo aquí.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Área de los Signals
        self.btn_suma.clicked.connect(self.sumar)
        self.btn_resta.clicked.connect(self.restar)
        self.btn_mult.clicked.connect(self.multiplicar)
        self.btn_division.clicked.connect(self.dividir)
        self.txt_resultado.setEnabled(False)

        # Área de los Slots

    def sumar(self):
        A = int(self.txt_x.text())
        B = int(self.txt_y.text())
        r = A + B
        self.txt_resultado.setText(str(r))

    def restar(self):
        A = int(self.txt_x.text())
        B = int(self.txt_y.text())
        r = A - B
        self.txt_resultado.setText(str(r))

    def multiplicar(self):
        A = int(self.txt_x.text())
        B = int(self.txt_y.text())
        r = A * B
        self.txt_resultado.setText(str(r))

    def dividir(self):
        A = int(self.txt_x.text())
        B = int(self.txt_y.text())
        r = A / B
        rr = round(r, 2)
        self.txt_resultado.setText(str(rr))

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())