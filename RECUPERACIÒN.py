import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from ui.recuperar_ui import Ui_MainWindow


class RecuperarContrasena(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.btn_recover.clicked.connect(self.recuperar_contrasena)
        self.ui.pushButton_2.clicked.connect(self.volver_atras)

    def recuperar_contrasena(self):
        correo = self.ui.lineEdit.text()

        if not correo:
            QMessageBox.warning(self, "Error", "Por favor, ingrese su correo electrónico.")
            return

        if "@" not in correo:
            QMessageBox.warning(self, "Error", "El correo electrónico no es válido.")
            return

        print(f"Enviando enlace de restablecimiento a {correo}")


        QMessageBox.information(self, "Éxito", f"Enlace de restablecimiento enviado a {correo}.")

    def volver_atras(self):

        self.close()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = RecuperarContrasena()
    ventana.show()
    sys.exit(app.exec_())
