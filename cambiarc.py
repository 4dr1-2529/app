import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from ui.cambiar_ui import Ui_MainWindow

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


        self.pushButton.clicked.connect(self.change_password)  # Ejemplo de conexión

    def change_password(self):

        old_password = self.lineEdit.text()
        new_password = self.lineEdit_2.text()
        confirm_password = self.lineEdit_3.text()

        if new_password == confirm_password:
            print("Contraseña cambiada exitosamente.")

        else:
            print("Las contraseñas no coinciden.")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
