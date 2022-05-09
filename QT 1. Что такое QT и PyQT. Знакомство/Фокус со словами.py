import sys

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit


class Focus(QWidget):

    def __init__(self):
        super().__init__()
        self.setGeometry(300, 300, 320, 60)
        self.setWindowTitle('Фокус со словами')
        self.tr1 = QLineEdit(self)
        self.tr1.setGeometry(10, 20, 125, 30)
        self.tr = QLineEdit(self)
        self.tr.setGeometry(175, 20, 125, 30)
        self.btn = QPushButton('->', self)
        self.btn.setGeometry(140, 20, 30, 30)
        self.btn.clicked.connect(self.word)

    def word(self):
        if self.btn.text() == '->':
            self.btn.setText('<-')
            self.tr.setText(self.tr1.text())
            self.tr1.setText('')

        else:
            self.btn.setText('->')
            self.tr1.setText(self.tr.text())
            self.tr.setText('')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Focus()
    ex.show()
    sys.exit(app.exec())
