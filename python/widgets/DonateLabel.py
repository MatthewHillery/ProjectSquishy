from PyQt5.QtWidgets import QLabel
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QCursor
from python.Constants import *


class DonateLabel(QLabel):
    def __init__(self, frame, name, q_rect):
        super().__init__(frame)
        self.setGeometry(q_rect)
        font = QFont()
        font.setFamily(FONT)
        font.setPointSize(FONT_SIZE)
        font.setBold(True)
        self.setFont(font)
        self.setCursor(QCursor(Qt.ArrowCursor))
        self.setScaledContents(False)
        self.setWordWrap(False)
        self.setObjectName(name)
