from PyQt5.QtWidgets import QComboBox
from PyQt5.QtGui import QFont


class ComboBox(QComboBox):
    def __init__(self):
        super().__init__()
        font = QFont()
        font.setFamily("Ariel")
        font.setPointSize(12)
        self.setFont(font)
        self.setFixedWidth(150)
        # self.activated.connect(self.do_something)

    def do_something(self):
        # fill_fields()
        print(self.currentText())
