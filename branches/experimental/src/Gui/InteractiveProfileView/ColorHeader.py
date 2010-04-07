from HeaderItem import *

class ColorHeader(HeaderItem):
    def __init__(self, parent, scene, rect, pos, font, profileColumn, textAngle):
        HeaderItem.__init__(self, parent, scene, rect, pos, font, profileColumn, textAngle)
        self.drawText(QCoreApplication.translate('color header', 'Color'))
