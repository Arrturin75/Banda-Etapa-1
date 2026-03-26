from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QHBoxLayout, QVBoxLayout, QLabel, QPushButton, QStackedWidget
import sys

from inicio import PantallaInicio
from produccion import PantallaProduccion
from conexion import PantallaConexion
from mantenimiento import PantallaMantenimiento
from historial import PantallaHistorial

from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont

class Ventana(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Sistema de Clasificación")
        self.setGeometry(100, 100, 900, 500)
        
        fuente = QFont("Felix Titling", 16, QFont.Weight.Bold, italic=True)

        contenedor = QWidget()
        self.setCentralWidget(contenedor)
        
        mi_layout = QVBoxLayout()

        self.titulo = QLabel("SISTEMA DE CLASIFICACIÓN AUTOMÁTICA")
        self.titulo.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.titulo.setFont(fuente)
        self.titulo.setFixedHeight(50)
        
        layout_horizontal = QHBoxLayout()
        
        self.stack = QStackedWidget()

        self.p_inicio = PantallaInicio()
        self.p_produccion = PantallaProduccion()
        self.p_conexion = PantallaConexion()
        self.p_mantenimiento = PantallaMantenimiento()
        self.p_historial = PantallaHistorial()

        self.stack.addWidget(self.p_inicio)        # 0
        self.stack.addWidget(self.p_produccion)    # 1
        self.stack.addWidget(self.p_conexion)      # 2
        self.stack.addWidget(self.p_mantenimiento) # 3
        self.stack.addWidget(self.p_historial)     # 4

        opciones = QVBoxLayout()

        self.inicio = QPushButton("INICIO")
        self.produccion = QPushButton("PRODUCCIÓN")
        self.conexion = QPushButton("CONEXIÓN")
        self.mantenimiento = QPushButton("MANTENIMIENTO")
        self.historial = QPushButton("HISTORIAL")
              
        self.inicio.clicked.connect(lambda: self.stack.setCurrentIndex(0))
        self.produccion.clicked.connect(lambda: self.stack.setCurrentIndex(1))
        self.conexion.clicked.connect(lambda: self.stack.setCurrentIndex(2))
        self.mantenimiento.clicked.connect(lambda: self.stack.setCurrentIndex(3))
        self.historial.clicked.connect(lambda: self.stack.setCurrentIndex(4))

        opciones.addWidget(self.inicio)
        opciones.addWidget(self.produccion)
        opciones.addWidget(self.conexion)
        opciones.addWidget(self.mantenimiento)
        opciones.addWidget(self.historial)
        
        opciones.addStretch()

        self.inicio.setFixedHeight(40)
        self.inicio.setFont(fuente)
        self.produccion.setFixedHeight(40)
        self.produccion.setFont(fuente)
        self.conexion.setFixedHeight(40)
        self.conexion.setFont(fuente)
        self.mantenimiento.setFixedHeight(40)
        self.mantenimiento.setFont(fuente)
        self.historial.setFixedHeight(40)
        self.historial.setFont(fuente)
                
        layout_horizontal.addLayout(opciones, 1)
        layout_horizontal.addWidget(self.stack, 4)

        mi_layout.addWidget(self.titulo)
        mi_layout.addLayout(layout_horizontal)

        contenedor.setLayout(mi_layout)

        self.setStyleSheet("""
            QMainWindow {
                background-color: #121212;
            }
            QLabel {
                color: white;
                background-color: #2c3e50;
            }
            QPushButton {
                background-color: #1f5f7a;
                color: white;
                border-radius: 3px;
            }
            QPushButton:hover {
                background-color: #2980b9;
            }
        """)     

def main():
    print("Iniciando el programa")
    app = QApplication(sys.argv)
    ventana = Ventana()
    ventana.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()