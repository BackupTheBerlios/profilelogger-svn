from HeaderItem import *

from PyQt4.QtGui import *
from PyQt4.QtCore import *

class FaciesHeaderItem(HeaderItem):
    def __init__(self, parent, scene, rect, pen):
        HeaderItem.__init__(self, parent, scene, rect, pen,
                            unicode(QCoreApplication.translate("Facies Label in Profile Header", "Facies")), -90)
