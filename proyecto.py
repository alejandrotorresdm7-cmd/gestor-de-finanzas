import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QMainWindow, QTabWidget, 
                             QVBoxLayout, QHBoxLayout, QLabel, QPushButton, 
                             QLineEdit, QComboBox, QTableWidget, QTableWidgetItem, 
                             QHeaderView, QFrame)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont, QDoubleValidator


COLOR_BG = "#1e1e2e"
COLOR_CARD = "#252538"
COLOR_TEXT = "#cdd6f4"
COLOR_ACCENT = "#89b4fa"
COLOR_GREEN = "#a6e3a1"
COLOR_RED = "#f38ba8"

class FinanzasApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("FinanzAsist - Gestor de Finanzas Personales")
        self.resize(800, 550)
        
       
        self.balance_total = 0.0
        
      
        self.init_ui()
        self.aplicar_estilos()

    def init_ui(self):
        
        self.tabs = QTabWidget()
        self.setCentralWidget(self.tabs)
        
       
        self.pestana_resumen = QWidget()
        self.pestana_registro = QWidget()
        
        self.tabs.addTab(self.pestana_resumen, "📊 Resumen General")
        self.tabs.addTab(self.pestana_registro, "➕ Registrar Movimiento")
        
       
        self.crear_pestana_resumen()
        self.crear_pestana_registro()

 
    def crear_pestana_resumen(self):
        layout = QVBoxLayout()
        
        
        self.card_balance = QFrame()
        self.card_balance.setObjectName("TarjetaBalance")
        card_layout = QVBoxLayout()
        
        lbl_titulo = QLabel("BALANCE TOTAL ACTUAL")
        lbl_titulo.setAlignment(Qt.AlignCenter)
        
        self.lbl_monto_balance = QLabel("$ 0.00")
        self.lbl_monto_balance.setAlignment(Qt.AlignCenter)
        self.lbl_monto_balance.setFont(QFont("Arial", 24, QFont.Bold))
        
        card_layout.addWidget(lbl_titulo)
        card_layout.addWidget(self.lbl_monto_balance)
        self.card_balance.setLayout(card_layout)
        
      
        lbl_historial = QLabel("Historial de Transacciones recientes:")
        lbl_historial.setFont(QFont("Arial", 11, QFont.Bold))
        
        self.tabla = QTableWidget()
        self.tabla.setColumnCount(4)
        self.tabla.setHorizontalHeaderLabels(["Tipo", "Categoría", "Monto", "Descripción"])
        self.tabla.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.tabla.setEditTriggers(QTableWidget.NoEditTriggers) 
        
        
        layout.addWidget(self.card_balance)
        layout.addSpacing(15)
        layout.addWidget(lbl_historial)
        layout.addWidget(self.tabla)
        
        self.pestana_resumen.setLayout(layout)

   
    def crear_pestana_registro(self):
        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignTop)
        
        lbl_instruccion = QLabel("Ingrese los datos del nuevo movimiento:")
        lbl_instruccion.setFont(QFont("Arial", 12, QFont.Bold))
        layout.addWidget(lbl_instruccion)
        layout.addSpacing(10)
        
      
        self.cb_tipo = QComboBox()
        self.cb_tipo.addItems(["Ingreso", "Gasto"])
        
        self.cb_categoria = QComboBox()
        self.cb_categoria.addItems(["Sueldo", "Comida", "Transporte", "Entretenimiento", "Otros"])
        
        self.input_monto = QLineEdit()
        self.input_monto.setPlaceholderText("Ej: 25.50")
       
        self.input_monto.setValidator(QDoubleValidator(0.00, 999999.99, 2, self))
        
        self.input_desc = QLineEdit()
        self.input_desc.setPlaceholderText("Ej: Pago de almuerzo o Alquiler")
        
       
        layout.addWidget(QLabel("Tipo de movimiento:"))
        layout.addWidget(self.cb_tipo)
        layout.addWidget(QLabel("Categoría:"))
        layout.addWidget(self.cb_categoria)
        layout.addWidget(QLabel("Monto ($):"))
        layout.addWidget(self.input_monto)
        layout.addWidget(QLabel("Descripción breve:"))
        layout.addWidget(self.input_desc)
        
        layout.addSpacing(20)
        
     
        btn_guardar = QPushButton("Guardar Transacción")
        btn_guardar.setObjectName("BtnGuardar")
        btn_guardar.clicked.connect(self.procesar_registro)
        layout.addWidget(btn_guardar)
        
        self.pestana_registro.setLayout(layout)

   
    def procesar_registro(self):
        
        texto_monto = self.input_monto.text().replace(",", ".")
        if not texto_monto:
            return
            
        tipo = self.cb_tipo.currentText()
        categoria = self.cb_categoria.currentText()
        monto = float(texto_monto)
        descripcion = self.input_desc.text() if self.input_desc.text() else "Sin descripción"
        
        
        if tipo == "Ingreso":
            self.balance_total += monto
        else:
            self.balance_total -= monto
            
       
        self.lbl_monto_balance.setText(f"$ {self.balance_total:.2f}")
        if self.balance_total >= 0:
            self.lbl_monto_balance.setStyleSheet(f"color: {COLOR_GREEN};")
        else:
            self.lbl_monto_balance.setStyleSheet(f"color: {COLOR_RED};")
            
       
        fila_actual = self.tabla.rowCount()
        self.tabla.insertRow(fila_actual)
        
       
        item_tipo = QTableWidgetItem(tipo)
        if tipo == "Ingreso":
            item_tipo.setForeground(Qt.green)
        else:
            item_tipo.setForeground(Qt.red)
            
        self.tabla.setItem(fila_actual, 0, item_tipo)
        self.tabla.setItem(fila_actual, 1, QTableWidgetItem(categoria))
        self.tabla.setItem(fila_actual, 2, QTableWidgetItem(f"$ {monto:.2f}"))
        self.tabla.setItem(fila_actual, 3, QTableWidgetItem(descripcion))
        
       
        self.input_monto.clear()
        self.input_desc.clear()
        self.tabs.setCurrentIndex(0)

 
    def aplicar_estilos(self):
        self.setStyleSheet(f"""
            QMainWindow {{
                background-color: {COLOR_BG};
            }}
            QTabWidget::pane {{
                border: 1px solid #444;
                background-color: {COLOR_BG};
            }}
            QTabBar::tab {{
                background: {COLOR_CARD};
                color: {COLOR_TEXT};
                padding: 10px 20px;
                border-top-left-radius: 4px;
                border-top-right-radius: 4px;
            }}
            QTabBar::tab:selected {{
                background: {COLOR_ACCENT};
                color: {COLOR_BG};
                font-weight: bold;
            }}
            QLabel {{
                color: {COLOR_TEXT};
            }}
            QFrame#TarjetaBalance {{
                background-color: {COLOR_CARD};
                border: 2px solid {COLOR_ACCENT};
                border-radius: 8px;
                padding: 10px;
            }}
            QLineEdit, QComboBox {{
                background-color: {COLOR_CARD};
                color: {COLOR_TEXT};
                border: 1px solid #555;
                border-radius: 4px;
                padding: 6px;
            }}
            QLineEdit:focus, QComboBox:focus {{
                border: 1px solid {COLOR_ACCENT};
            }}
            QTableWidget {{
                background-color: {COLOR_CARD};
                color: {COLOR_TEXT};
                gridline-color: #444;
                border-radius: 4px;
            }}
            QHeaderView::section {{
                background-color: #313244;
                color: {COLOR_TEXT};
                padding: 5px;
                border: 1px solid #222;
            }}
            QPushButton#BtnGuardar {{
                background-color: {COLOR_ACCENT};
                color: {COLOR_BG};
                font-weight: bold;
                font-size: 14px;
                padding: 10px;
                border-radius: 6px;
            }}
            QPushButton#BtnGuardar:hover {{
                background-color: #b4befe;
            }}
        """)

def run():
    app = QApplication(sys.argv)
    ventana = FinanzasApp()
    ventana.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    run()
