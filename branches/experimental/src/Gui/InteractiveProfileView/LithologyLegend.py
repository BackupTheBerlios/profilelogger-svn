from LegendItemGroup import *

from LithologyLegendItem import *

class LithologyLegend(LegendItemGroup):
    def __init__(self, parent, scene, rect, pos, headerFont, legendFont, profile):
        LegendItemGroup.__init__(self, 
                                 parent, 
                                 scene, 
                                 rect, 
                                 pos, 
                                 headerFont, 
                                 legendFont,
                                 unicode(QCoreApplication.translate('legend header', 'Lithologies')), 
                                 profile)
        itmW = self.rect().width() / self.profile.colsInLegend
        col = 0
        for l in self.profile.project.lithologies:
            itm = LithologyLegendItem(self, self.scene(),
                                      QRectF(0, 0, itmW, 1.5*itmW),
                                      QPointF(itmW * col, self.y),
                                      self.legendFont,
                                      l)
            col += 1
            if col == self.profile.colsInLegend:
                col = 0
                self.y += itm.rect().height()
        self.y += 1.5*itmW
        w = self.rect().width()        
        self.setRect(QRectF(0, 0, w, self.y))
