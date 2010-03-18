from GraphicsRectItem import *

from LegendItem import *
from HeaderItem import *
from ColumnItem import *

class ProfileItem(GraphicsRectItem):
    def __init__(self, parent, scene, profile):
        GraphicsRectItem.__init__(self, parent, scene)
        self.profile = profile
        self.internalSpacing = 25 #pixel
        self.drawingWidth = 600
        
        self.legendItem = LegendItem(self, scene)
        self.legendItem.setRect(0, 0, self.drawingWidth, 500)

        self.headerItem = HeaderItem(self, scene)
        self.headerItem.setRect(0, 0, self.drawingWidth, 50)
        
        self.columnItem = ColumnItem(self, scene)
        self.columnItem.setRect(0, 0, self.drawingWidth, 1000)

        self.legendItem.setPos(0, 0)
        self.headerItem.setPos(0, 
                               self.legendItem.pos().y() + self.legendItem.boundingRect().height() + self.internalSpacing)
        self.columnItem.setPos(0, self.headerItem.pos().y() + self.headerItem.boundingRect().height() + self.internalSpacing)
