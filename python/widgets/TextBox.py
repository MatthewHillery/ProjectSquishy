from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt


class TextBox(QLineEdit):
    def __init__(self):
        super().__init__()
        font = QFont()
        font.setFamily("Ariel") # TODO: COme up with font
        font.setPointSize(12)
        self.setFixedWidth(100)
        self.setAlignment(Qt.AlignCenter)
        self.setFont(font)
