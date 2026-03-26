from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout,
    QLabel, QPushButton, QSpinBox,
    QComboBox, QSlider, QProgressBar
)
from PyQt6.QtCore import Qt


class PantallaProduccion(QWidget):
    def __init__(self):
        super().__init__()

        main_layout = QVBoxLayout()

        config_layout = QVBoxLayout()

        meta_layout = QHBoxLayout()
        label_meta = QLabel("Meta total:")
        self.spin_meta = QSpinBox()
        self.spin_meta.setRange(1, 1000)
        self.spin_meta.setValue(100)

        meta_layout.addWidget(label_meta)
        meta_layout.addWidget(self.spin_meta)

        tipo_layout = QHBoxLayout()
        label_tipo = QLabel("Tipo producto:")
        self.combo_tipo = QComboBox()
        self.combo_tipo.addItems(["ROJO", "VERDE", "TODOS"])

        tipo_layout.addWidget(label_tipo)
        tipo_layout.addWidget(self.combo_tipo)

        vel_layout = QHBoxLayout()
        label_vel = QLabel("Velocidad:")
        self.slider_vel = QSlider(Qt.Orientation.Horizontal)
        self.slider_vel.setRange(0, 100)
        self.slider_vel.setValue(50)

        self.label_vel_valor = QLabel("50%")

        vel_layout.addWidget(label_vel)
        vel_layout.addWidget(self.slider_vel)
        vel_layout.addWidget(self.label_vel_valor)

        btn_layout = QHBoxLayout()

        self.btn_aplicar = QPushButton("APLICAR")
        self.btn_iniciar = QPushButton("INICIAR")

        btn_layout.addWidget(self.btn_aplicar)
        btn_layout.addWidget(self.btn_iniciar)

        progreso_layout = QVBoxLayout()

        self.barra = QProgressBar()
        self.barra.setValue(0)

        self.label_progreso = QLabel("0 / 100 piezas")
        self.label_progreso.setAlignment(Qt.AlignmentFlag.AlignCenter)

        progreso_layout.addWidget(self.barra)
        progreso_layout.addWidget(self.label_progreso)

        config_layout.addLayout(meta_layout)
        config_layout.addLayout(tipo_layout)
        config_layout.addLayout(vel_layout)

        main_layout.addLayout(config_layout)
        main_layout.addSpacing(15)
        main_layout.addLayout(btn_layout)
        main_layout.addSpacing(20)
        main_layout.addLayout(progreso_layout)

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
            QProgressBar {
                height: 25px;
                background-color: #333;
            }
            QProgressBar::chunk {
                background-color: #00FFAA;
            }
        """)

        self.slider_vel.valueChanged.connect(self.actualizar_velocidad)
        self.btn_aplicar.clicked.connect(self.aplicar_config)
        self.btn_iniciar.clicked.connect(self.iniciar_produccion)

    def actualizar_velocidad(self, valor):
        self.label_vel_valor.setText(f"{valor}%")

    def aplicar_config(self):
        meta = self.spin_meta.value()
        tipo = self.combo_tipo.currentText()
        vel = self.slider_vel.value()

        print(f"Meta: {meta}, Tipo: {tipo}, Velocidad: {vel}%")

    def iniciar_produccion(self):
        self.barra.setValue(50)
        meta = self.spin_meta.value()
        self.label_progreso.setText(f"50 / {meta} piezas")