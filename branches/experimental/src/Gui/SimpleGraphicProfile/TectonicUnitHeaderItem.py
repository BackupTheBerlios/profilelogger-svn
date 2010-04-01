from HeaderItem import *

from PyQt4.QtGui import *
from PyQt4.QtCore import *

class TectonicUnitHeaderItem(HeaderItem):
    def __init__(self, parent, scene, rect, pen):
        HeaderItem.__init__(self, parent, scene, rect, pen,
                            unicode(QCoreApplication.translate("Tectonic Unit Label in Profile Header", "Tectonic Unit")), -90)
