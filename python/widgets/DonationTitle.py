from PyQt5.QtWidgets import QLabel
from PyQt5.QtGui import QFont
from PyQt5.QtCore import QRect

from python.Constants import *


class DonationTitle(QLabel):
    def __init__(self, frame):
        super().__init__(frame)
        self.setGeometry(QRect(130, 10, 71, 31))
        font = QFont()
        font.setFamily(FONT)
        font.setPointSize(16)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.setFont(font)
        self.setObjectName(TITLE_LABEL_ID)
