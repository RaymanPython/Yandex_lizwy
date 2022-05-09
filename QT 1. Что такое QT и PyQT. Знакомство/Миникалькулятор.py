from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtWidgets import QLCDNumber, QLabel, QLineEdit
import sys


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        x = 200
        y = 20
        dx = 80
        dy = 20
        self.setGeometry(300, 300, 400, 120)
        self.setWindowTitle('Первая программа')

        self.btn = QPushButton('->', self)
        self.btn.move(120, 50)
        self.btn.clicked.connect(self.run)

        self.first_input = QLineEdit(self)
        self.first_input.move(20, 20)

        self.second_input = QLineEdit(self)
        self.second_input.move(20, 80)

        self.summ_lbl = QLabel(self)
        self.summ_lbl.setText(" " * (len("Произведение:") - len("Сумма:")) + "Сумма:")
        self.summ_lbl.move(x, y)

        self.summ = QLCDNumber(self)
        self.summ.move(x + dx, y)

        self.ras_lbl = QLabel(self)
        self.ras_lbl.setText(" " * (len("Произведение:") - len("Разность:")) + "Разность:")
        self.ras_lbl.move(x, y + dy)

        self.ras = QLCDNumber(self)
        self.ras.move(x + dx, y + dy)

        self.chas_lbl = QLabel(self)
        self.chas_lbl.setText(" " * (len("Произведение:") - len("Частное:")) + "Частное:")
        self.chas_lbl.move(x, y + 2 * dy)

        self.chas = QLCDNumber(self)
        self.chas.move(x + dx, y + 2 * dy)

        self.prois_lbl = QLabel(self)
        self.prois_lbl.setText("Произведение:")
        self.prois_lbl.move(x, y + 3 * dy)

        self.prois = QLCDNumber(self)
        self.prois.move(x + dx, y + 3 * dy)
        self.prois.move(x + dx, y + 3 * dy)

    def run(self):
        x, y = list(map(int, [self.first_input.text(), self.second_input.text()]))
        self.summ.display(x + y)
        self.ras.display(x - y)
        if y != 0:
            self.chas.display(x / y)
        else:
            self.chas.display("ERROR")
        self.prois.display(x * y)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
