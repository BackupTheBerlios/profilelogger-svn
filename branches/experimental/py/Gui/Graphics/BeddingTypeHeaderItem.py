from HeaderItem import *

from PyQt4.QtGui import *
from PyQt4.QtCore import *

class BeddingTypeHeaderItem(HeaderItem):
    def __init__(self, parent, scene, rect, pen):
        HeaderItem.__init__(self, parent, scene, rect, pen,
                            unicode(QCoreApplication.translate("Bedding Type Label in Profile Header", "Bedding Types")), -90)
