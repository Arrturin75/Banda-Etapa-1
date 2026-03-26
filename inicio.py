from PyQt6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QProgressBar
from PyQt6.QtCore import Qt

class Led(QLabel):
    def __init__(self, color="red"):
        super().__init__()
        self.setFixedSize(25, 25)
        self.set_color(color)

    def set_color(self, color):
        self.setStyleSheet(f"""
            background-color: {color};
            border-radius: 12px;
            border: 2px solid black;
        """)


class PantallaInicio(QWidget):
    def __init__(self):
        super().__init__()

        main_layout = QVBoxLayout()

        estado_layout = QHBoxLayout()

        self.led = Led("red")
        self.label_estado = QLabel("STOP")
        self.label_estado.setStyleSheet("font-size: 20px;")

        estado_layout.addWidget(self.led)
        estado_layout.addWidget(self.label_estado)
        estado_layout.addStretch()

        cont_layout = QVBoxLayout()

        self.label_rojo = QLabel("ROJO: 0")
        self.label_verde = QLabel("VERDE: 0")

        self.label_rojo.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_verde.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.label_rojo.setStyleSheet("font-size: 28px;")
        self.label_verde.setStyleSheet("font-size: 28px;")

        cont_layout.addWidget(self.label_rojo)
        cont_layout.addWidget(self.label_verde)

        self.barra = QProgressBar()
        self.barra.setValue(0)

        btn_layout = QHBoxLayout()

        self.btn_start = QPushButton("START")
        self.btn_stop = QPushButton("STOP")
        self.btn_reset = QPushButton("RESET")

        btn_layout.addWidget(self.btn_start)
        btn_layout.addWidget(self.btn_stop)
        btn_layout.addWidget(self.btn_reset)

        main_layout.addLayout(estado_layout)
        main_layout.addSpacing(20)
        main_layout.addLayout(cont_layout)
        main_layout.addSpacing(20)
        main_layout.addWidget(self.barra)
        main_layout.addSpacing(20)
        main_layout.addLayout(btn_layout)

        self.setLayout(main_layout)
        
        self.setStyleSheet("""
            QLabel {
                color: #00FFAA;
            }
            QPushButton {
                background-color: #007ACC;
                color: white;
                font-size: 16px;
                padding: 10px;
                border-radius: 5px;
            }
            QPushButton:hover {
                background-color: #005A9E;
            }
            QProgressBar {
                height: 25px;
                background-color: #333;
                color: white;
            }
            QProgressBar::chunk {
                background-color: #00FFAA;
            }
        """)

        # =========================
        # 🔌 FUNCIONES (TEMPORALES)
        # =========================
        self.btn_start.clicked.connect(self.iniciar)
        self.btn_stop.clicked.connect(self.detener)
        self.btn_reset.clicked.connect(self.reset)

    def iniciar(self):
        self.label_estado.setText("RUN")
        self.led.set_color("green")

    def detener(self):
        self.label_estado.setText("STOP")
        self.led.set_color("red")

    def reset(self):
        self.label_rojo.setText("ROJO: 0")
        self.label_verde.setText("VERDE: 0")
        self.barra.setValue(0)