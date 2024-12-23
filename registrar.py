import sys
from PyQt5.QtWidgets import QApplication, QDialog, QMessageBox
from ui.registro_ui import Ui_Dialog

class RegistroUsuario(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)


        self.ui.pushButton.clicked.connect(self.registrar_usuario)
        self.ui.pushButton_2.clicked.connect(self.cancelar_registro)

    def registrar_usuario(self):

        nombre_usuario = self.ui.lineEdit.text()
        correo = self.ui.lineEdit_2.text()
        contrasena = self.ui.lineEdit_3.text()
        confirmar_contrasena = self.ui.lineEdit_4.text()


        if not nombre_usuario or not correo or not contrasena or not confirmar_contrasena:
            QMessageBox.warning(self, "Error", "Por favor, complete todos los campos.")
            return

        if contrasena != confirmar_contrasena:
            QMessageBox.warning(self, "Error", "Las contraseñas no coinciden.")
            return

        if "@" not in correo:
            QMessageBox.warning(self, "Error", "El correo electrónico no es válido.")
            return


        print("Usuario registrado:", nombre_usuario, correo)
        QMessageBox.information(self, "Éxito", "Registro exitoso.")

    def cancelar_registro(self):

        self.ui.lineEdit.clear()
        self.ui.lineEdit_2.clear()
        self.ui.lineEdit_3.clear()
        self.ui.lineEdit_4.clear()
        self.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    dialog = RegistroUsuario()
    dialog.exec_()
    sys.exit(app.exec_())
