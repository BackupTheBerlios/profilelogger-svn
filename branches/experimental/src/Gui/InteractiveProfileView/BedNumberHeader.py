from HeaderItem import *

class BedNumberHeader(HeaderItem):
    def __init__(self, parent, scene, rect, pos, font, profileColumn, textAngle):
        HeaderItem.__init__(self, parent, scene, rect, pos, font, profileColumn, textAngle)
        self.drawText(QCoreApplication.translate('bed number hearder', 'Bed Number'))
