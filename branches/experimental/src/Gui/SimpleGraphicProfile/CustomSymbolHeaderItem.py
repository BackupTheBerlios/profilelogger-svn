from HeaderItem import *

from PyQt4.QtGui import *
from PyQt4.QtCore import *

class CustomSymbolHeaderItem(HeaderItem):
    def __init__(self, parent, scene, rect, pen):
        HeaderItem.__init__(self, parent, scene, rect, pen,
                            unicode(QCoreApplication.translate("Custom Symbol Label in Profile Header", "Custom\nSymbols")), -90)
