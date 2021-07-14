from PyQt5.QtWidgets import QPushButton
from PyQt5.QtGui import QFont
from python.Constants import *


class DonateButton(QPushButton):
    def __init__(self, frame, name, q_rect):
        super().__init__(frame)
        self.setGeometry(q_rect)
        font = QFont()
        font.setFamily(FONT)
        font.setPointSize(FONT_SIZE)
        font.setBold(True)
        font.setItalic(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.setFont(font)
        self.setAutoFillBackground(False)
        self.setStyleSheet("color: red;")
        self.setShortcut("")
        self.setObjectName(name)
