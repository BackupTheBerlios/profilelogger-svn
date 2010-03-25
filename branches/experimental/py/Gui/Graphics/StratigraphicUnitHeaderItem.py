from HeaderItem import *

from PyQt4.QtGui import *
from PyQt4.QtCore import *

class StratigraphicUnitHeaderItem(HeaderItem):
    def __init__(self, parent, scene, rect, pen):
        HeaderItem.__init__(self, parent, scene, rect, pen,
                            unicode(QCoreApplication.translate("Stratigraphic Unit Label in Profile Header", "Stratigraphic Unit")), -90)
