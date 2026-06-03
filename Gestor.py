from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QLabel, QPushButton, QLineEdit
from PyQt5.QtCore import Qt


ANCHO, ALTO = 700, 400
TITULO = "Gestor de finanzas PyQt5"
text_btn = "Enviar"
text_input = "Ingrese un monto o descripción..."

class MainWindow(QWidget):
    def __init__(self, parent=None, flags=Qt.WindowFlags()):
        super().__init__(parent=parent, flags=flags)
        
        
        self.set_Window()
        self.config_Window()
        self.event_handler()

    def set_Window(self):
        
        self.btn = QPushButton(text_btn)
        self.texto = QLabel("Historial: ") 
        self.input = QLineEdit()
        self.input.setPlaceholderText(text_input)

        
        self.main_layout = QHBoxLayout()
        
        
        self.main_layout.addWidget(self.input, alignment=Qt.AlignLeft)
        self.main_layout.addWidget(self.btn, alignment=Qt.AlignLeft)
        self.main_layout.addWidget(self.texto, alignment=Qt.AlignLeft)

        self.setLayout(self.main_layout)

    def config_Window(self):
        self.resize(ANCHO, ALTO)
        self.setWindowTitle(TITULO)

    def event_handler(self):
        
        self.btn.clicked.connect(self.set_text)
        
    def set_text(self):
        
        cadena = self.input.text()
        if cadena: 
            self.texto.setText(f"Registro: {cadena}")
            self.input.clear()

def run():
    app = QApplication([])
   
    main_window = MainWindow()
    main_window.show() 
    app.exec_()

if __name__ == "__main__":
    run()
