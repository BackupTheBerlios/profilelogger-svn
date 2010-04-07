from HeaderItem import *

class CustomSymbolHeader(HeaderItem):
    def __init__(self, parent, scene, rect, pos, font, profileColumn, textAngle):
        HeaderItem.__init__(self, parent, scene, rect, pos, font, profileColumn, textAngle)
        self.drawText(QCoreApplication.translate('custom Symbol header', 'Custom Symbol'))
