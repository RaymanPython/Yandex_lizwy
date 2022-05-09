fimport
sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow


class widget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('Текстовый флаг.ui', self)
        self.initUI()

    def initUI(self):
        self.a = ''
        self.b = ''
        self.c = ''
        self.FG1.buttonClicked[int].connect(self.on_button_clicked1)
        self.SG2.buttonClicked[int].connect(self.on_button_clicked2)
        self.TG3.buttonClicked[int].connect(self.on_button_clicked3)
        self.pushButton.clicked.connect(self.vivod)
        self.label.setText('   ')

    def on_button_clicked1(self, id):
        for button in self.FG1.buttons():
            if button is self.FG1.button(id):
                self.a = button.text()

    def on_button_clicked2(self, id):
        for button in self.SG2.buttons():
            if button is self.SG2.button(id):
                self.b = button.text()

    def on_button_clicked3(self, id):
        for button in self.TG3.buttons():
            if button is self.TG3.button(id):
                self.c = button.text()

    def vivod(self):
        self.label.setText('Цвета: ' + self.a + ', ' + self.b + ' и ' + self.c)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = widget()
    ex.show()
    sys.exit(app.exec_())

```
< ?xml
version = "1.0"
encoding = "UTF-8"? >
< ui
version = "4.0" >
<

class >MainWindow < / class >

< widget


class ="QMainWindow" name="MainWindow" >

< property
name = "enabled" >
< bool > true < / bool >
< / property >
< property
name = "geometry" >
< rect >
< x > 0 < / x >
< y > 0 < / y >
< width > 550 < / width >
< height > 330 < / height >
< / rect >
< / property >
< property
name = "minimumSize" >
< size >
< width > 550 < / width >
< height > 330 < / height >
< / size >
< / property >
< property
name = "maximumSize" >
< size >
< width > 550 < / width >
< height > 300 < / height >
< / size >
< / property >
< property
name = "focusPolicy" >
< enum > Qt::NoFocus < / enum >
< / property >
< property
name = "windowTitle" >
< string > MainWindow < / string >
< / property >
< widget


class ="QWidget" name="centralwidget" >

< widget


class ="QRadioButton" name="radioButton" >

< property
name = "geometry" >
< rect >
< x > 80 < / x >
< y > 120 < / y >
< width > 82 < / width >
< height > 17 < / height >
< / rect >
< / property >
< property
name = "text" >
< string > Синий < / string >
< / property >
< attribute
name = "buttonGroup" >
< string
notr = "true" > FG1 < / string >
< / attribute >
< / widget >
< widget


class ="QRadioButton" name="radioButton_2" >

< property
name = "geometry" >
< rect >
< x > 80 < / x >
< y > 140 < / y >
< width > 81 < / width >
< height > 21 < / height >
< / rect >
< / property >
< property
name = "text" >
< string > Красный < / string >
< / property >
< attribute
name = "buttonGroup" >
< string
notr = "true" > FG1 < / string >
< / attribute >
< / widget >
< widget


class ="QRadioButton" name="radioButton_3" >

< property
name = "geometry" >
< rect >
< x > 80 < / x >
< y > 160 < / y >
< width > 82 < / width >
< height > 17 < / height >
< / rect >
< / property >
< property
name = "text" >
< string > Зеленый < / string >
< / property >
< attribute
name = "buttonGroup" >
< string
notr = "true" > FG1 < / string >
< / attribute >
< / widget >
< widget


class ="QLabel" name="FG1_2" >

< property
name = "geometry" >
< rect >
< x > 100 < / x >
< y > 90 < / y >
< width > 47 < / width >
< height > 13 < / height >
< / rect >
< / property >
< property
name = "text" >
< string > Цвет1 < / string >
< / property >
< / widget >
< widget


class ="QRadioButton" name="radioButton_10" >

< property
name = "geometry" >
< rect >
< x > 240 < / x >
< y > 150 < / y >
< width > 82 < / width >
< height > 17 < / height >
< / rect >
< / property >
< property
name = "text" >
< string > Зеленый < / string >
< / property >
< attribute
name = "buttonGroup" >
< string
notr = "true" > SG2 < / string >
< / attribute >
< / widget >
< widget


class ="QLabel" name="SG2_2" >

< property
name = "geometry" >
< rect >
< x > 260 < / x >
< y > 80 < / y >
< width > 47 < / width >
< height > 13 < / height >
< / rect >
< / property >
< property
name = "text" >
< string > Цвет
2 < / string >
< / property >
< / widget >
< widget


class ="QRadioButton" name="radioButton_11" >

< property
name = "geometry" >
< rect >
< x > 240 < / x >
< y > 130 < / y >
< width > 81 < / width >
< height > 21 < / height >
< / rect >
< / property >
< property
name = "text" >
< string > Красный < / string >
< / property >
< attribute
name = "buttonGroup" >
< string
notr = "true" > SG2 < / string >
< / attribute >
< / widget >
< widget


class ="QRadioButton" name="radioButton_12" >

< property
name = "geometry" >
< rect >
< x > 240 < / x >
< y > 110 < / y >
< width > 82 < / width >
< height > 17 < / height >
< / rect >
< / property >
< property
name = "text" >
< string > Синий < / string >
< / property >
< attribute
name = "buttonGroup" >
< string
notr = "true" > SG2 < / string >
< / attribute >
< / widget >
< widget


class ="QRadioButton" name="radioButton_13" >

< property
name = "geometry" >
< rect >
< x > 370 < / x >
< y > 150 < / y >
< width > 82 < / width >
< height > 17 < / height >
< / rect >
< / property >
< property
name = "text" >
< string > Зеленый < / string >
< / property >
< attribute
name = "buttonGroup" >
< string
notr = "true" > TG3 < / string >
< / attribute >
< / widget >
< widget


class ="QLabel" name="TG3_2" >

< property
name = "geometry" >
< rect >
< x > 390 < / x >
< y > 80 < / y >
< width > 47 < / width >
< height > 13 < / height >
< / rect >
< / property >
< property
name = "text" >
< string > Цвет
3 < / string >
< / property >
< / widget >
< widget


class ="QRadioButton" name="radioButton_14" >

< property
name = "geometry" >
< rect >
< x > 370 < / x >
< y > 130 < / y >
< width > 81 < / width >
< height > 21 < / height >
< / rect >
< / property >
< property
name = "text" >
< string > Красный < / string >
< / property >
< attribute
name = "buttonGroup" >
< string
notr = "true" > TG3 < / string >
< / attribute >
< / widget >
< widget


class ="QRadioButton" name="radioButton_15" >

< property
name = "geometry" >
< rect >
< x > 370 < / x >
< y > 110 < / y >
< width > 82 < / width >
< height > 16 < / height >
< / rect >
< / property >
< property
name = "text" >
< string > Синий < / string >
< / property >
< attribute
name = "buttonGroup" >
< string
notr = "true" > TG3 < / string >
< / attribute >
< / widget >
< widget


class ="QPushButton" name="pushButton" >

< property
name = "geometry" >
< rect >
< x > 354 < / x >
< y > 200 < / y >
< width > 151 < / width >
< height > 23 < / height >
< / rect >
< / property >
< property
name = "text" >
< string > Сделать
флаг < / string >
< / property >
< / widget >
< widget


class ="QLabel" name="label" >

< property
name = "geometry" >
< rect >
< x > 90 < / x >
< y > 280 < / y >
< width > 281 < / width >
< height > 16 < / height >
< / rect >
< / property >
< property
name = "text" >
< string / >
< / property >
< / widget >
< / widget >
< widget


class ="QMenuBar" name="menubar" >

< property
name = "geometry" >
< rect >
< x > 0 < / x >
< y > 0 < / y >
< width > 550 < / width >
< height > 21 < / height >
< / rect >
< / property >
< / widget >
< widget


class ="QStatusBar" name="statusbar" / >

< / widget >
< resources / >
< connections / >
< buttongroups >
< buttongroup
name = "FG1" / >
< buttongroup
name = "SG2" / >
< buttongroup
name = "TG3" / >
< / buttongroups >
< / ui >
```
