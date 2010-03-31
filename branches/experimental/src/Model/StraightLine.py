from Dataset import Dataset

from PyQt4.QtGui import *
from PyQt4.QtCore import *

class StraightLine(Dataset):
    def __init__(self, id=None, drawing=None,
                 x1=0, y1=0, x2=0, y2=0,
                 pen=None):
        Dataset.__init__(self, id)
        self.drawing = drawing
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.pen = pen
    def makeLine(self):
        return QLineF(self.x1, self.y1, self.x2, self.y2)
    def hasPen(self):
        return self.pen is not None
