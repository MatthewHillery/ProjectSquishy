from PyQt5.QtWidgets import QCheckBox
from PyQt5.QtCore import QSize


class Checkbox(QCheckBox):
    def __init__(self, frame, name, q_rect):
        super().__init__(frame)
        self.setGeometry(q_rect)
        self.setText("")
        self.setIconSize(QSize(24, 24))
        self.setChecked(False)
        self.setTristate(False)
        self.setObjectName(name)
