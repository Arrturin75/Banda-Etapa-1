class PantallaVacia(QWidget):
    def __init__(self, texto):
        super().__init__()
        layout = QVBoxLayout()
        label = QLabel(texto)
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(label)
        self.setLayout(layout)

