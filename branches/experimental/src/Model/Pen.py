from NamedDescribedDataset import *

from PyQt4.QtGui import *

class Pen(NamedDescribedDataset):
    def __init__(self, id=None, name=None, description=None,
                 rgbRed=0, rgbGreen=0, rgbBlue=0, rgbAlpha=255,
                 width=1, 
                 penCapStyle=None, penJoinStyle=None, penStyle=None, 
                 brush=None):
        NamedDescribedDataset.__init__(self, id, name, description)
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
    def hasPenCapStyle(self):
        return self.penCapStyle is not None
    def hasPenJoinStyle(self):
        return self.penJoinStyle is not None
    def hasPenStyle(self):
        return self.penStyle is not None
    def hasBrush(self):
        return self.brush is not None
    def hasWidth(self):
        return self.width > 0
    def getQPen(self):
        p = QPen(self.getColor())
        if self.hasPenCapStyle():
            p.setCapStyle(self.penCapStyle.enumFromEnumValue())
        if self.hasPenJoinStyle():
            p.setJoinStyle(self.penJoinStyle.enumFromEnumValue())
        if self.hasPenStyle():
            p.setStyle(self.penStyle.enumFromEnumValue())
        if self.hasBrush():
            p.setBrush(self.brush.getQBrush())
        if self.hasWidth():
            p.setWidth(self.width)
        return p
