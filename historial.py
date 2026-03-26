from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout,
    QLabel, QPushButton, QTextEdit, QComboBox
)
from PyQt6.QtCore import Qt
from datetime import datetime

class PantallaHistorial(QWidget):
    def __init__(self):
        super().__init__()

        main_layout = QVBoxLayout()

        filtros_layout = QHBoxLayout()

        self.combo_tiempo = QComboBox()
        self.combo_tiempo.addItems(["HOY", "TODO"])

        self.combo_tipo = QComboBox()
        self.combo_tipo.addItems(["TODO", "EVENTOS", "ERRORES"])

        filtros_layout.addWidget(QLabel("Tiempo:"))
        filtros_layout.addWidget(self.combo_tiempo)
        filtros_layout.addWidget(QLabel("Tipo:"))
        filtros_layout.addWidget(self.combo_tipo)
        filtros_layout.addStretch()

        self.log = QTextEdit()
        self.log.setReadOnly(True)

        resumen_layout = QVBoxLayout()

        self.label_total = QLabel("Total producidas: 0")
        self.label_tiempo = QLabel("Tiempo activo: 00:00")

        resumen_layout.addWidget(self.label_total)
        resumen_layout.addWidget(self.label_tiempo)

        btn_layout = QHBoxLayout()

        self.btn_exportar = QPushButton("EXPORTAR")
        self.btn_limpiar = QPushButton("LIMPIAR")

        btn_layout.addWidget(self.btn_exportar)
        btn_layout.addWidget(self.btn_limpiar)

        main_layout.addLayout(filtros_layout)
        main_layout.addWidget(self.log)
        main_layout.addLayout(resumen_layout)
        main_layout.addLayout(btn_layout)

        self.setLayout(main_layout)

        self.setStyleSheet("""
            QLabel {
                color: #00FFAA;
                font-size: 14px;
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

        self.btn_limpiar.clicked.connect(self.limpiar_log)
        self.btn_exportar.clicked.connect(self.exportar_log)

        self.agregar_evento("Sistema iniciado")

    def agregar_evento(self, texto):
        hora = datetime.now().strftime("%H:%M:%S")
        self.log.append(f"[{hora}] {texto}")

    def limpiar_log(self):
        self.log.clear()

    def exportar_log(self):
        print("Exportando historial (puedes guardar en archivo después)")