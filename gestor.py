from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QLabel, QPushButton, QLineEdit
from PyQt5.QtCore import Qt

# Tus variables globales originales (corregido el typo de texto_input)
ANCHO, ALTO = 700, 400
TITULO = "Gestor de finanzas PyQt5"
text_btn = "Enviar"
text_input = "Ingrese un monto o descripción..."

class MainWindow(QWidget):
    def __init__(self, parent=None, flags=Qt.WindowFlags()):
        super().__init__(parent=parent, flags=flags)
        
        # Llamamos a tus funciones en el orden correcto para construir la app
        self.set_Window()
        self.config_Window()
        self.event_handler()

    def set_Window(self):
        # Tus componentes originales (corregidas las mayúsculas de QLineEdit)
        self.btn = QPushButton(text_btn)
        self.texto = QLabel("Historial: ") # Le damos un texto inicial para que sepa qué es
        self.input = QLineEdit()
        self.input.setPlaceholderText(text_input) # Usamos tu variable para el fondo del input

        # Tu layout horizontal (corregido el typo de QHBoxLayout)
        self.main_layout = QHBoxLayout()
        
        # Corregida la sintaxis para añadir los widgets al layout usando .addWidget
        self.main_layout.addWidget(self.input, alignment=Qt.AlignLeft)
        self.main_layout.addWidget(self.btn, alignment=Qt.AlignLeft)
        self.main_layout.addWidget(self.texto, alignment=Qt.AlignLeft)

        self.setLayout(self.main_layout)

    def config_Window(self):
        self.resize(ANCHO, ALTO)
        self.setWindowTitle(TITULO)

    def event_handler(self):
        # Conectamos el clic de tu botón con tu función set_text
        self.btn.clicked.connect(self.set_text)
        
    def set_text(self):
        # Tu lógica original: toma el texto del input y lo pone en la etiqueta (QLabel)
        cadena = self.input.text()
        if cadena: # Validamos que no esté vacío
            self.texto.setText(f"Registro: {cadena}")
            self.input.clear() # Limpia el input para una nueva entrada

def run():
    app = QApplication([])
    # Corregido el typo "main:window = MianWindow()" por una asignación limpia
    main_window = MainWindow()
    main_window.show() # Añadido para que la ventana se vuelva visible
    app.exec_()

if __name__ == "__main__":
    run()
