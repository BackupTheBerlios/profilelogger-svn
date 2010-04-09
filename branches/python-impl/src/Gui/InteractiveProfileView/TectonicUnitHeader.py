from HeaderItem import *

class TectonicUnitHeader(HeaderItem):
    def __init__(self, parent, scene, rect, pos, font, profileColumn, textAngle):
        HeaderItem.__init__(self, parent, scene, rect, pos, font, profileColumn, textAngle)
        self.drawText(QCoreApplication.translate('tectonic Unit header', 'Tectonic Unit'))
