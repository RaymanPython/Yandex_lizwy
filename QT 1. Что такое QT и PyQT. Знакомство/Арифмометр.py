import sys
from PyQt5.QtWidgets import QWidget, QLabel, QPushButton, QLineEdit, QApplication


class Example(QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(300, 200, 320, 60)
        self.setWindowTitle('Арифмометр')

        self.first_input_value = QLineEdit("0", self)
        self.first_input_value.move(10, 10)
        self.first_input_value.resize(30, 30)

        self.second_input_value = QLineEdit("0", self)
        self.second_input_value.move(180, 10)
        self.second_input_value.resize(30, 30)

        self.output_value = QLineEdit(self)
        self.output_value.move(250, 10)
        self.output_value.resize(30, 30)
        self.output_value.setEnabled(False)

        self.sum_btn = QPushButton('+', self)
        self.sum_btn.resize(30, 30)
        self.sum_btn.move(50, 10)
        self.sum_btn.clicked.connect(self.go_sum)

        self.subtraction_btn = QPushButton('-', self)
        self.subtraction_btn.resize(30, 30)
        self.subtraction_btn.move(80, 10)
        self.subtraction_btn.clicked.connect(self.go_subtraction)

        self.multiplication_btn = QPushButton('*', self)
        self.multiplication_btn.resize(30, 30)
        self.multiplication_btn.move(110, 10)
        self.multiplication_btn.clicked.connect(self.go_multiplication)

    def go_sum(self):
        self.output_value.setText(str(float(self.first_input_value.text()) + float(self.second_input_value.text())))

    def go_subtraction(self):
        self.output_value.setText(str(float(self.first_input_value.text()) - float(self.second_input_value.text())))

    def go_multiplication(self):
        self.output_value.setText(str(float(self.first_input_value.text()) * float(self.second_input_value.text())))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec_())
