from PyQt4.QtGui import *
from PyQt4.QtCore import *

class GraphicsScene(QGraphicsScene):
    def __init__(self, parent):
        QGraphicsScene.__init__(self, parent)
