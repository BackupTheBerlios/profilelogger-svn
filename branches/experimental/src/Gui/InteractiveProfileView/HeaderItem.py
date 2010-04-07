from RectItem import *

from TextItem import *

class HeaderItem(RectItem):
    def __init__(self, parent, scene, rect, pos, font, profileColumn, textAngle):
        RectItem.__init__(self, parent, scene, rect, pos)
        self.font = font
        self.profileColumn = profileColumn
        self.textAngle = textAngle
        self.setPen(QPen(Qt.black))
    def drawText(self, txt):
        self.txtItm = TextItem(self, self.font)
        self.txtItm.setText(txt)
        self.txtItm.setRotation(self.textAngle)
        self.txtItm.adjustSize()
        if self.textAngle is not None:
            self.txtItm.setPos(QPointF((self.rect().width() - self.txtItm.boundingRect().height()) / 2, 
                                       self.rect().height()))
        else:
            self.txtItm.setPos(QPointF((self.rect().width() - self.txtItm.boundingRect().width()) / 2, 
                                       self.rect().height() - self.txtItm.boundingRect().height()))
