from HeaderItem import *

from PyQt4.QtGui import *
from PyQt4.QtCore import *

class FossilHeaderItem(HeaderItem):
    def __init__(self, parent, scene, rect, pen):
        HeaderItem.__init__(self, parent, scene, rect, pen,
                            unicode(QCoreApplication.translate("Fossil Label in Profile Header", "Fossil")), -90)