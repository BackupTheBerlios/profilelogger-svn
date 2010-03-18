from PyQt4.QtGui import *
from PyQt4.QtCore import *

class CanvasView(QGraphicsView):
    def __init__(self, parent):
        QGraphicsView.__init__(self, parent)
        self.setMinimumSize(500, 500)
