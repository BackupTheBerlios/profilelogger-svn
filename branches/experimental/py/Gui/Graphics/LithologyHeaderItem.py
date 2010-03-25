from HeaderItem import *

from PyQt4.QtGui import *
from PyQt4.QtCore import *

class LithologyHeaderItem(HeaderItem):
    def __init__(self, parent, scene, rect, pen):
        HeaderItem.__init__(self, parent, scene, rect, pen,
                            unicode(QCoreApplication.translate("Lithology Label in Profile Header", "Lithology")), -90)
