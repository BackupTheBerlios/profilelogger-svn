from HeaderItem import *

from PyQt4.QtGui import *
from PyQt4.QtCore import *

class OutcropTypeHeaderItem(HeaderItem):
    def __init__(self, parent, scene, rect, pen):
        HeaderItem.__init__(self, parent, scene, rect, pen,
                            unicode(QCoreApplication.translate("Outcrop Type Label in Profile Header", "Outcrop Type")), -90)
