import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from ui.iniciar_ui import Ui_MainWindow


class IniciarSesion(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Conectar los botones usando los nombres correctos
        self.ui.btn_login.clicked.connect(self.iniciar_sesion)  # Botón para iniciar sesión
        self.ui.pushButton_2.clicked.connect(self.abrir_crear_cuenta)  # Botón para crear cuenta
        self.ui.pushButton.clicked.connect(self.abrir_cambiar_contrasena)  # Botón para cambiar contraseña
        self.ui.pushButton_3.clicked.connect(self.abrir_recuperar_contrasena)  # Botón para recuperar contraseña

    def iniciar_sesion(self):
        # Lógica para iniciar sesión
        print("Iniciando sesión...")

    def abrir_crear_cuenta(self):
        # Lógica para abrir la ventana de creación de cuenta
        print("Abriendo la ventana para crear cuenta...")

    def abrir_cambiar_contrasena(self):
        # Lógica para abrir la ventana de cambio de contraseña
        print("Abriendo la ventana para cambiar contraseña...")

    def abrir_recuperar_contrasena(self):
        # Lógica para abrir la ventana de recuperación de contraseña
        print("Abriendo la ventana para recuperar contraseña...")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = IniciarSesion()
    window.show()
    sys.exit(app.exec_())
