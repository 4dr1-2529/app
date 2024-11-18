import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from ui.iniciar_ui import Ui_MainWindow


class IniciarSesion(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)


        self.ui.btn_login.clicked.connect(self.iniciar_sesion)
        self.ui.pushButton_2.clicked.connect(self.abrir_crear_cuenta)
        self.ui.pushButton.clicked.connect(self.abrir_cambiar_contrasena)
        self.ui.pushButton_3.clicked.connect(self.abrir_recuperar_contrasena)

    def iniciar_sesion(self):

        print("Iniciando sesión...")

    def abrir_crear_cuenta(self):
        print("Abriendo la ventana para crear cuenta...")

    def abrir_cambiar_contrasena(self):
        print("Abriendo la ventana para cambiar contraseña...")

    def abrir_recuperar_contrasena(self):
        print("Abriendo la ventana para recuperar contraseña...")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = IniciarSesion()
    window.show()
    sys.exit(app.exec_())
