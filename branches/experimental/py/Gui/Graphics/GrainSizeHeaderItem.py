from HeaderItem import *

from PyQt4.QtGui import *
from PyQt4.QtCore import *

class GrainSizeHeaderItem(HeaderItem):
    def __init__(self, parent, scene, rect, pen):
        HeaderItem.__init__(self, parent, scene, rect, pen,
                            unicode(QCoreApplication.translate("Grain Size Label in Profile Header", "Grain Size")), 0)
