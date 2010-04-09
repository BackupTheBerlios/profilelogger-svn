from HeaderItem import *

from PyQt4.QtGui import *
from PyQt4.QtCore import *

class BedHeaderItem(HeaderItem):
    def __init__(self, parent, scene, rect, pen):
        HeaderItem.__init__(self, parent, scene, rect, pen,
                            unicode(QCoreApplication.translate("Bed Label in Profile Header", "Bed Number")), -90)
