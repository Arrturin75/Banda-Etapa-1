from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout,
    QLabel, QPushButton
)
from PyQt6.QtCore import Qt

class PantallaMantenimiento(QWidget):
    def __init__(self):
        super().__init__()

        main_layout = QVBoxLayout()

        control_layout = QVBoxLayout()

        banda_layout = QHBoxLayout()
        label_banda = QLabel("Banda:")

        self.btn_banda_on = QPushButton("ON")
        self.btn_banda_off = QPushButton("OFF")

        banda_layout.addWidget(label_banda)
        banda_layout.addWidget(self.btn_banda_on)
        banda_layout.addWidget(self.btn_banda_off)

        valv1_layout = QHBoxLayout()
        label_valv1 = QLabel("Válvula 1:")
        self.btn_valv1 = QPushButton("ACTIVAR")
        self.btn_valv12 = QPushButton("DESACTIVAR")

        valv1_layout.addWidget(label_valv1)
        valv1_layout.addWidget(self.btn_valv1)
        valv1_layout.addWidget(self.btn_valv12)

        valv2_layout = QHBoxLayout()
        label_valv2 = QLabel("Válvula 2:")
        self.btn_valv2 = QPushButton("ACTIVAR")
        self.btn_valv21 = QPushButton("DESACTIVAR")

        valv2_layout.addWidget(label_valv2)
        valv2_layout.addWidget(self.btn_valv2)
        valv2_layout.addWidget(self.btn_valv21)

        sensores_layout = QVBoxLayout()

        self.label_sensor_color = QLabel("Sensor color: ---")
        self.label_sensor_paso = QLabel("Sensor paso: ---")

        sensores_layout.addWidget(self.label_sensor_color)
        sensores_layout.addWidget(self.label_sensor_paso)

        acciones_layout = QVBoxLayout()

        self.btn_prueba = QPushButton("PRUEBA GENERAL")
        self.btn_emergencia = QPushButton("PARO DE EMERGENCIA")

        acciones_layout.addWidget(self.btn_prueba)
        acciones_layout.addWidget(self.btn_emergencia)

        control_layout.addLayout(banda_layout)
        control_layout.addLayout(valv1_layout)
        control_layout.addLayout(valv2_layout)

        main_layout.addLayout(control_layout)
        main_layout.addSpacing(15)
        main_layout.addLayout(sensores_layout)
        main_layout.addSpacing(15)
        main_layout.addLayout(acciones_layout)

        self.setLayout(main_layout)

        self.setStyleSheet("""
            QLabel {
                color: #00FFAA;
                font-size: 16px;
            }
            QPushButton {
                background-color: #007ACC;
                color: white;
                padding: 10px;
                border-radius: 5px;
            }
            QPushButton:hover {
                background-color: #005A9E;
            }
        """)

        self.btn_emergencia.setStyleSheet("""
            background-color: red;
            color: white;
            font-size: 16px;
            padding: 12px;
            border-radius: 5px;
        """)

        self.btn_banda_on.clicked.connect(self.banda_on)
        self.btn_banda_off.clicked.connect(self.banda_off)
        self.btn_valv1.clicked.connect(self.activar_valvula1)
        self.btn_valv12.clicked.connect(self.desactivar_valvula1)
        self.btn_valv2.clicked.connect(self.activar_valvula2)
        self.btn_valv21.clicked.connect(self.desactivar_valvula1)
        self.btn_prueba.clicked.connect(self.prueba_general)
        self.btn_emergencia.clicked.connect(self.paro_emergencia)

    def banda_on(self):
        print("Banda ON")

    def banda_off(self):
        print("Banda OFF")

    def activar_valvula1(self):
        print("Válvula 1 activada")

    def desactivar_valvula1(self):
        print("Válvula 1 desactivada")

    def activar_valvula2(self):
        print("Válvula 2 activada")

    def desactivar_valvula2(self):
        print("Válvula 2 desactivada")

    def prueba_general(self):
        print("Ejecutando prueba general")

    def paro_emergencia(self):
        print("!!! PARO DE EMERGENCIA !!!")