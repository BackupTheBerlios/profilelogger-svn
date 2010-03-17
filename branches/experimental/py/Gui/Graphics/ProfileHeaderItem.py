from GraphicsRectItem import GraphicsRectItem

class ProfileHeaderItem(GraphicsRectItem):
    def __init__(self, parent):
        GraphicsRectItem.__init__(self, parent)
    def setProfile(self, p):
        self.profile = p
        self.setPen(QPen(Qt.black))
        setRect(QRectF(0, 0, 100, 00))
