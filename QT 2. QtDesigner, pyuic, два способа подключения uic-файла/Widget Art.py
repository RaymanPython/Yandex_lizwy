import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow


class widget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('Записная книжка.ui', self)
        self.initUI()

    def initUI(self):
        self.pushButton.clicked.connect(self.otvet)

    def otvet(self):
        self.a = self.lineEdit.text()
        self.b = self.lineEdit_2.text()
        self.c = str(self.b) + ' ' + str(self.a)
        self.listWidget.addItem(self.c)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = widget()
    ex.show()
    sys.exit(app.exec_())
