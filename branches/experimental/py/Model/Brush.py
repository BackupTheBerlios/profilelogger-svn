from NamedDescribedDataset import *

from PyQt4.QtGui import *

class Brush(NamedDescribedDataset):
    def __init__(self, id=None, name=None, description=None,
                 rgbRed=0, rgbGreen=0, rgbBlue=0, rgbAlpha=255,
                 brushStyle=None):
        NamedDescribedDataset.__init__(self, id, name, description)
        self.rgbRed = rgbRed
        self.rgbGreen = rgbGreen
        self.rgbBlue = rgbBlue
        self.rgbAlpha = rgbAlpha
        self.brushStyle = brushStyle
    def getColor(self):
        return QColor(self.rgbRed, self.rgbGreen, self.rgbBlue, self.rgbAlpha)
    def hasBrushStyle(self):
        return self.brushStyle is not None
    def getQBrush(self):
        b = QBrush(self.getColor())
        if self.hasBrushStyle():
            b.setStyle(self.brushStyle.enumFromEnumValue())
        return b
