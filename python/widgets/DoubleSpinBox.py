from PyQt5.QtWidgets import QDoubleSpinBox
from PyQt5.QtGui import QFont
from python.Constants import *


class DoubleSpinBox(QDoubleSpinBox):
    def __init__(self, frame, name, q_rect, min_val, max_val, default, step):
        super().__init__(frame)
        self.setGeometry(q_rect)
        font = QFont()
        font.setFamily(FONT)
        font.setPointSize(FONT_SIZE)
        self.setFont(font)
        self.setWrapping(False)
        self.setFrame(True)
        self.setProperty("showGroupSeparator", False)
        self.setMinimum(min_val)
        self.setMaximum(max_val)
        self.setSingleStep(step)
        self.setProperty("value", default)
        self.setObjectName(name)
