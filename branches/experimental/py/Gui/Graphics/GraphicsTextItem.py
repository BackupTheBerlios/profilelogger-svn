from PyQt4.QtGui import *

class GraphicsTextItem(QGraphicsTextItem):
    def __init__(self, parent, scene, text):
        QGraphicsTextItem.__init__(self, parent, scene)
        self.setText(text)
