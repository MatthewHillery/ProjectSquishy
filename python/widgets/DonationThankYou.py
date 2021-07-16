from PyQt5.QtWidgets import QLabel
from PyQt5.QtGui import QFont
from PyQt5.QtCore import QRect
from python.Constants import *


class DonationThankYou(QLabel):
    def __init__(self, frame):
        super().__init__(frame)
        self.setGeometry(QRect(20, 45, 250, 30))
        font = QFont()
        font.setFamily(FONT)
        font.setPointSize(FONT_SIZE)
        self.setFont(font)
        self.setObjectName(THANK_YOU_LABEL_ID)
