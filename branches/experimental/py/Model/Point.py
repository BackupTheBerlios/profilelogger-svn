from Dataset import Dataset

from PyQt4.QtCore import *

class Point(Dataset):
    def __init__(self, id=None, x=0, y=0):
        Dataset.__init__(self, id)
        self.x = x
        self.y = y
    def toPoint(self):
        return QPointF(self.x, self.y)
