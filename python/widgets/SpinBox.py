from PyQt5.QtWidgets import QSpinBox
from PyQt5.QtGui import QFont
from python.Constants import *


class SpinBox(QSpinBox):
    def __init__(self, frame, name, q_rect, min_val, max_val, default, step):
        super().__init__(frame)
        self.setGeometry(q_rect)
        font = QFont()
        font.setFamily(FONT)
        font.setPointSize(FONT_SIZE)
        self.setFont(font)
        self.setMinimum(min_val)
        self.setMaximum(max_val)
        self.setProperty("value", default)
        self.setSingleStep(step)
        self.setDisplayIntegerBase(10)
        self.setObjectName(name)