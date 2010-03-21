from PyQt4.QtGui import *
from PyQt4.QtCore import *

class PathItem(QGraphicsPathItem):
    def __init__(self, parent, scene, path=None):
        QGraphicsPathItem.__init__(self, parent, scene)
        if path is not None:
            self.setPath(path)
