import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from ui.cambiar_ui import Ui_MainWindow  # Importa la clase desde el archivo UI

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)  # Configura la UI generada por Qt Designer

        # Conectar los botones a sus funciones
        self.pushButton.clicked.connect(self.change_password)  # Ejemplo de conexión

    def change_password(self):
        # Lógica para cambiar la contraseña
        old_password = self.lineEdit.text()
        new_password = self.lineEdit_2.text()
        confirm_password = self.lineEdit_3.text()

        if new_password == confirm_password:
            print("Contraseña cambiada exitosamente.")
            # Aquí iría la lógica de cambio de contraseña (actualizar base de datos, etc.)
        else:
            print("Las contraseñas no coinciden.")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()  # Muestra la ventana principal
    sys.exit(app.exec_())  # Ejecuta el ciclo de eventos de la aplicación
