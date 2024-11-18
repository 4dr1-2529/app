import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from ui.recuperar_ui import Ui_MainWindow


class RecuperarContrasena(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Conectar los botones
        self.ui.btn_recover.clicked.connect(self.recuperar_contrasena)  # Botón "Enviar Enlace"
        self.ui.pushButton_2.clicked.connect(self.volver_atras)  # Botón "Atrás"

    def recuperar_contrasena(self):
        # Obtener el correo ingresado
        correo = self.ui.lineEdit.text()

        # Validar que el correo no esté vacío
        if not correo:
            QMessageBox.warning(self, "Error", "Por favor, ingrese su correo electrónico.")
            return

        # Validación simple de formato de correo
        if "@" not in correo:
            QMessageBox.warning(self, "Error", "El correo electrónico no es válido.")
            return

        # Aquí podrías agregar la lógica para enviar el enlace de restablecimiento al correo (simulado en este caso)
        print(f"Enviando enlace de restablecimiento a {correo}")

        # Mostrar mensaje de éxito
        QMessageBox.information(self, "Éxito", f"Enlace de restablecimiento enviado a {correo}.")

    def volver_atras(self):
        # Cerrar la ventana actual
        self.close()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = RecuperarContrasena()
    ventana.show()
    sys.exit(app.exec_())
