from HeaderItem import *

from PyQt4.QtGui import *
from PyQt4.QtCore import *

class LithologicalUnitHeaderItem(HeaderItem):
    def __init__(self, parent, scene, rect, pen):
        HeaderItem.__init__(self, parent, scene, rect, pen,
                            unicode(QCoreApplication.translate("Lithological Unit Label in Profile Header", "Lithologic Unit")), -90)
