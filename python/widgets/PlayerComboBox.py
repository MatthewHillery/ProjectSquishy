from PyQt5.QtWidgets import QComboBox
from PyQt5.QtGui import QFont
from PyQt5.QtCore import QRect
from PyQt5.QtCore import QSize
from PyQt5.QtCore import Qt
from python.Constants import *


class PlayerComboBox(QComboBox):
    def __init__(self, frame):
        super().__init__(frame)
        self.setGeometry(QRect(10, 30, 271, 30))
        self.setMaximumSize(QSize(16777214, 16777215))
        font = QFont()
        font.setFamily(FONT)
        font.setPointSize(FONT_SIZE)
        self.setFont(font)
        self.setLayoutDirection(Qt.LeftToRight)
        self.setObjectName("player_combo_box")
