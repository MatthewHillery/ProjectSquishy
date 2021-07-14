from PyQt5.QtWidgets import QPushButton
from PyQt5.QtGui import QFont
from python.Constants import *


class Button(QPushButton):
    def __init__(self, frame, name, q_rect):
        super().__init__(frame)
        self.setGeometry(q_rect)
        font = QFont()
        font.setFamily(FONT)
        font.setPointSize(FONT_SIZE)
        self.setFont(font)
        self.setShortcut("")
        self.setObjectName(name)
