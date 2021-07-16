from PyQt5.QtWidgets import QLabel
from PyQt5.QtGui import QFont
from python.Constants import *


class DonationAddress(QLabel):
    def __init__(self, frame, name, q_rect):
        super().__init__(frame)
        self.setGeometry(q_rect)
        font = QFont()
        font.setFamily(FONT)
        font.setPointSize(9)
        self.setFont(font)
        self.setObjectName(name)

