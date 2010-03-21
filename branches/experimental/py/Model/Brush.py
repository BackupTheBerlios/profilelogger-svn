from NamedDescribedDataset import *

from PyQt4.QtGui import QColor

class Brush(NamedDescribedDataset):
    def __init__(self, id=None, name=None, description=None,
                 rgbRed=0, rgbGreen=0, rgbBlue=0, rgbAlpha=255,
                 brushStyle=None):
        NamedDescribedDataset.__init__(id, name, description)
        self.rgbRed = rgbRed
        self.rgbGreen = rgbGreen
        self.rgbBlue = rgbBlue
        self.rgbAlpha = rgbAlpha
        self.brushStyle = brushStyle
    def getColor(self):
        return QColor(self.rgbRed, self.rgbGreen, self.rgbBlue, self.rgbAlpha)
