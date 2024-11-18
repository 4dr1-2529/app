import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QStackedWidget, QWidget, QPushButton, QMessageBox
from cambiarc import CambiarContraseña  # Importa el archivo cambiarc.py
from iniciar import IniciarSesion  # Importa el archivo iniciar.py
from recuperacion import RecuperacionContraseña  # Importa el archivo recuperacion.py
from registrar import RegistroUsuario  # Importa el archivo registrar.py


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Aplicación Principal")
        self.setGeometry(100, 100, 400, 400)

        # Crear el widget para manejar las interfaces
        self.stacked_widget = QStackedWidget(self)
        self.setCentralWidget(self.stacked_widget)

        # Inicializar las pantallas
        self.init_login_screen()
        self.init_register_screen()
        self.init_recover_password_screen()
        self.init_change_password_screen()

    def init_login_screen(self):
        """Interfaz de Inicio de Sesión"""
        self.login_screen = QMainWindow(self)
        self.login_screen.setWindowTitle("Iniciar sesión")
        self.login_screen.setGeometry(100, 100, 400, 400)

        # Crear la interfaz de login
        self.login_ui = IniciarSesion()
        self.login_ui.setupUi(self.login_screen)

        # Conectar botones
        self.login_ui.recover_button.clicked.connect(self.show_recover_password_screen)
        self.login_ui.change_password_button.clicked.connect(self.show_change_password_screen)
        self.login_ui.register_button.clicked.connect(self.show_register_screen)

        # Añadir la pantalla de login al stacked widget
        self.stacked_widget.addWidget(self.login_screen)

    def init_register_screen(self):
        """Interfaz de Registro"""
        self.register_screen = QMainWindow(self)
        self.register_screen.setWindowTitle("Registro de Usuario")
        self.register_screen.setGeometry(100, 100, 400, 400)

        # Crear la interfaz de registro
        self.register_ui = RegistroUsuario()
        self.register_ui.setupUi(self.register_screen)

        # Añadir la pantalla de registro al stacked widget
        self.stacked_widget.addWidget(self.register_screen)

    def init_recover_password_screen(self):
        """Interfaz de Recuperación de Contraseña"""
        self.recover_screen = QMainWindow(self)
        self.recover_screen.setWindowTitle("Recuperar Contraseña")
        self.recover_screen.setGeometry(100, 100, 400, 400)

        # Crear la interfaz de recuperación de contraseña
        self.recover_ui = RecuperacionContraseña()
        self.recover_ui.setupUi(self.recover_screen)

        # Añadir la pantalla de recuperación al stacked widget
        self.stacked_widget.addWidget(self.recover_screen)

    def init_change_password_screen(self):
        """Interfaz de Cambiar Contraseña"""
        self.change_screen = QMainWindow(self)
        self.change_screen.setWindowTitle("Cambiar Contraseña")
        self.change_screen.setGeometry(100, 100, 400, 400)

        # Crear la interfaz de cambiar contraseña
        self.change_ui = CambiarContraseña()
        self.change_ui.setupUi(self.change_screen)

        # Añadir la pantalla de cambiar contraseña al stacked widget
        self.stacked_widget.addWidget(self.change_screen)

    def show_recover_password_screen(self):
        """Muestra la pantalla de recuperación de contraseña"""
        self.stacked_widget.setCurrentWidget(self.recover_screen)

    def show_change_password_screen(self):
        """Muestra la pantalla de cambiar contraseña"""
        self.stacked_widget.setCurrentWidget(self.change_screen)

    def show_register_screen(self):
        """Muestra la pantalla de registro"""
        self.stacked_widget.setCurrentWidget(self.register_screen)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
