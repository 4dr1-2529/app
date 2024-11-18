import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
# Importa la clase Ui_MainWindow desde el archivo iniciar.ui.py en la carpeta ui
from ui.iniciar_ui import Ui_MainWindow

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)  # Configura la UI (esto inicializa todos los elementos definidos en el .ui)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()  # Crear la instancia de la ventana principal
    window.show()  # Mostrar la ventana principal
    sys.exit(app.exec_())  # Iniciar el bucle de eventos de la aplicación
