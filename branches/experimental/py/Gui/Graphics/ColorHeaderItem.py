from HeaderItem import *

from PyQt4.QtGui import *
from PyQt4.QtCore import *

class ColorHeaderItem(HeaderItem):
    def __init__(self, parent, scene, rect, pen):
        HeaderItem.__init__(self, parent, scene, rect, pen,
                            unicode(QCoreApplication.translate("Color Label in Profile Header", "Colors")), -90)
