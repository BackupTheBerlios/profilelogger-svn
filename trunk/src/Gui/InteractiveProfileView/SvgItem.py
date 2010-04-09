from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PyQt4.QtSvg import *

class SvgItem(QGraphicsSvgItem):
    def __init__(self, parent, scene, maxSize, pos, svgData):
        QGraphicsSvgItem.__init__(self, parent, scene)
