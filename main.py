import sys
from random import randint

from PyQt5.QtWidgets import QWidget, QApplication, QPushButton
from PyQt5.QtGui import QPainter, QColor


class Suprematism(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.coords_ = []
        self.qp = QPainter()
        self.flag = False

    def initUI(self):
        self.setGeometry(300, 300, 1000, 1000)
        self.setWindowTitle('Суперматизм')
        self.setMouseTracking(True)
        self.btn = QPushButton('Кнопка', self)
        self.btn.resize(100, 100)
        self.btn.move(100, 100)
        self.btn.clicked.connect(self.drawf)

    def drawf(self):
        self.flag = True
        self.update()

    def paintEvent(self, event):
        if self.flag:
            self.qp = QPainter()
            self.qp.begin(self)
            self.draw()
            self.qp.end()

    def draw(self):
        R = randint(20, 100)
        c = randint(0, 255)
        c1 = randint(20, 255)
        c2 = randint(20, 255)
        self.qp.setBrush(QColor(c, c1, c2))
        self.coords_ = [randint(0, 1000), randint(0, 1000)]
        self.qp.drawEllipse(int(self.coords_[0] - R / 2), int(self.coords_[1] - R / 2), R, R)

    def keyPressEvent(self, event):
        self.drawf()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Suprematism()
    ex.show()
    sys.exit(app.exec())