from HeaderItem import *

from PyQt4.QtGui import *
from PyQt4.QtCore import *

class SedimentStructureHeaderItem(HeaderItem):
    def __init__(self, parent, scene, rect, pen):
        HeaderItem.__init__(self, parent, scene, rect, pen,
                            unicode(QCoreApplication.translate("Sediment Structure Label in Profile Header", "Sediment\nStructures")), -90)
