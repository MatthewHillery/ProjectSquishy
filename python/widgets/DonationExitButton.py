from PyQt5.QtWidgets import QPushButton
from PyQt5.QtGui import QFont
from PyQt5.QtCore import QRect
from python.Constants import *


class DonationExitButton(QPushButton):
    def __init__(self, frame):
        super().__init__(frame)
        self.setGeometry(QRect(300, 10, 21, 21))
        font = QFont()
        font.setFamily(FONT)
        font.setPointSize(FONT_SIZE)
        self.setFont(font)
        font.setBold(True)
        font.setWeight(75)
        self.setStyleSheet(DONATION_EXIT_BUTTON_CSS)
        self.setObjectName("exit_button")
