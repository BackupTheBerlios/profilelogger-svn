from NamedDescribedDataset import *

from PyQt4.QtGui import QColor

class Pen(NamedDescribedDataset):
    def __init__(self, id=None, name=None, description=None,
                 rgbRed=0, rgbGreen=0, rgbBlue=0, rgbAlpha=255,
                 width=1, 
                 penCapStyle=None, penJoinStyle=None, penStyle=None, 
                 brush=None):
        NamedDescribedDataset.__init__(id, name, description)
        self.rgbRed = rgbRed
        self.rgbGreen = rgbGreen
        self.rgbBlue = rgbBlue
        self.rgbAlpha = rgbAlpha
        self.width = width
        self.penCapStyle = penCapStyle
        self.penJoinStyle = penJoinStyle
        self.penStyle = penStyle
        self.brush = brush
    def getColor(self):
        return QColor(self.rgbRed, self.rgbGreen, self.rgbBlue, self.rgbAlpha)
