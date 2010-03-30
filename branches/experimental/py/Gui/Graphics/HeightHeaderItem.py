from HeaderItem import *

from PyQt4.QtGui import *
from PyQt4.QtCore import *

class HeightHeaderItem(HeaderItem):
    def __init__(self, parent, scene, rect, pen):
        HeaderItem.__init__(self, parent, scene, rect, pen,
                            unicode(QCoreApplication.translate("Height Label in Profile Header", "Total Height [mm]")), -90)
