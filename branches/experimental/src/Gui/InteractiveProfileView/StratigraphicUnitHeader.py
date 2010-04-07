from HeaderItem import *

class StratigraphicUnitHeader(HeaderItem):
    def __init__(self, parent, scene, rect, pos, font, profileColumn, textAngle):
        HeaderItem.__init__(self, parent, scene, rect, pos, font, profileColumn, textAngle)
        self.drawText(QCoreApplication.translate('stratigraphic Unit header', 'Stratigraphic Unit'))
