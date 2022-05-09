import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QWidget, QApplication
import math


class Form(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('calc.ui', self)
        self.screen = ''
        self.data = ''
        for i in self.buttonGroup_digits.buttons():
            i.clicked.connect(self.run)
        self.btn_clear.clicked.connect(self.clear)
        for i in self.buttonGroup_binary.buttons():
            i.clicked.connect(self.operation)
        self.btn_eq.clicked.connect(self.result)

    def clear(self):
        self.screen = ''
        self.data = ''
        self.table.display(0)

    def run(self):
        if self.data and self.data[-1].isdigit():
            self.screen += self.sender().text()
        else:
            self.screen = self.sender().text()
        self.data += self.sender().text()
        print(self.data)
        self.table.display(int(self.screen))

    def operation(self):
        if self.data and self.data[-1].isdigit():
            self.data += self.sender().text()
        elif self.data[-1] in '+-*/':
            self.data = self.data[:-1] + self.sender().text()
        print(self.data)

    def result(self):
        self.screen = str(eval(self.data))
        self.data = str(self.screen)
        self.table.display(float(self.screen))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = Form()
    form.show()
    sys.exit(app.exec())
