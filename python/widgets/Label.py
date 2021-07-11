from PyQt5.QtWidgets import QLabel
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt


class Label(QLabel):
    def __init__(self):
        super().__init__()
        font = QFont()
        font.setFamily("Ariel") # TODO: COme up with font
        font.setPointSize(12)
        self.setAlignment(Qt.AlignRight)
        self.setFont(font)
