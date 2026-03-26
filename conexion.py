from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout,
    QLabel, QPushButton, QComboBox, QTextEdit
)
from PyQt6.QtCore import Qt, QTimer
import serial
import serial.tools.list_ports

class PantallaConexion(QWidget):
    def __init__(self):
        super().__init__()

        self.ser = None

        main_layout = QVBoxLayout()

        config_layout = QVBoxLayout()

        puerto_layout = QHBoxLayout()
        label_puerto = QLabel("Puerto:")
        self.combo_puertos = QComboBox()
        self.actualizar_puertos()

        puerto_layout.addWidget(label_puerto)
        puerto_layout.addWidget(self.combo_puertos)

        baud_layout = QHBoxLayout()
        label_baud = QLabel("Baudrate:")
        self.combo_baud = QComboBox()
        self.combo_baud.addItems(["9600", "115200"])

        baud_layout.addWidget(label_baud)
        baud_layout.addWidget(self.combo_baud)

        btn_layout = QHBoxLayout()

        self.btn_conectar = QPushButton("CONECTAR")
        self.btn_desconectar = QPushButton("DESCONECTAR")
        self.btn_actualizar = QPushButton("ACTUALIZAR")

        btn_layout.addWidget(self.btn_conectar)
        btn_layout.addWidget(self.btn_desconectar)
        btn_layout.addWidget(self.btn_actualizar)

        estado_layout = QHBoxLayout()
        self.label_estado = QLabel("DESCONECTADO")
        self.label_estado.setStyleSheet("color: red;")

        estado_layout.addWidget(QLabel("Estado:"))
        estado_layout.addWidget(self.label_estado)
        estado_layout.addStretch()

        self.monitor = QTextEdit()
        self.monitor.setReadOnly(True)

        config_layout.addLayout(puerto_layout)
        config_layout.addLayout(baud_layout)
        config_layout.addLayout(btn_layout)
        config_layout.addLayout(estado_layout)

        main_layout.addLayout(config_layout)
        main_layout.addWidget(self.monitor)

        self.setLayout(main_layout)

        self.setStyleSheet("""
            QLabel {
                color: #00FFAA;
                font-size: 16px;
            }
            QPushButton {
                background-color: #007ACC;
                color: white;
                padding: 8px;
                border-radius: 5px;
            }
            QPushButton:hover {
                background-color: #005A9E;
            }
            QTextEdit {
                background-color: black;
                color: #00FF00;
                font-family: Consolas;
            }
        """)

        self.btn_conectar.clicked.connect(self.conectar)
        self.btn_desconectar.clicked.connect(self.desconectar)
        self.btn_actualizar.clicked.connect(self.actualizar_puertos)

        self.timer = QTimer()
        self.timer.timeout.connect(self.leer_datos)
        self.timer.start(300)

    def actualizar_puertos(self):
        self.combo_puertos.clear()
        puertos = serial.tools.list_ports.comports()
        for puerto in puertos:
            self.combo_puertos.addItem(puerto.device)

    def conectar(self):
        puerto = self.combo_puertos.currentText()
        baud = int(self.combo_baud.currentText())

        try:
            self.ser = serial.Serial(puerto, baud, timeout=1)
            self.label_estado.setText("CONECTADO")
            self.label_estado.setStyleSheet("color: green;")
            self.monitor.append(">> Conectado")
        except Exception as e:
            self.monitor.append(f"ERROR: {e}")

    def desconectar(self):
        if self.ser:
            self.ser.close()
            self.ser = None
            self.label_estado.setText("DESCONECTADO")
            self.label_estado.setStyleSheet("color: red;")
            self.monitor.append(">> Desconectado")

    def leer_datos(self):
        if self.ser and self.ser.in_waiting:
            try:
                dato = self.ser.readline().decode().strip()
                if dato:
                    self.monitor.append(f"<< {dato}")
            except:
                pass