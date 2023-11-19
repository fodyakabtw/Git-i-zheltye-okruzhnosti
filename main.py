import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QGraphicsScene, QGraphicsView, QGraphicsEllipseItem, QMainWindow
from PyQt5.QtGui import QColor
from PyQt5.QtCore import Qt
import random


class CircleApp(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.scene = QGraphicsScene(self)
        self.view = QGraphicsView(self.scene)
        self.verticalLayout.addWidget(self.view)
        self.btnCreateCircle.clicked.connect(self.createCircle)

    def createCircle(self):
        diameter = random.randint(20, 100)
        x = random.randint(0, self.view.width() - diameter)
        y = random.randint(0, self.view.height() - diameter)
        circle = QGraphicsEllipseItem(x, y, diameter, diameter)
        circle.setBrush(QColor(Qt.yellow))
        self.scene.addItem(circle)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = CircleApp()
    ex.show()
    sys.exit(app.exec_())
