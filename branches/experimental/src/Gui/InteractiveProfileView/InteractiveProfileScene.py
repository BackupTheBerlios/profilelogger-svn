from PyQt4.QtCore import *
from PyQt4.QtGui import *

from ProfileItem import *

class InteractiveProfileScene(QGraphicsScene):
    enableViews = pyqtSignal()
    disableViews = pyqtSignal()
    def __init__(self, parent):
        QGraphicsScene.__init__(self, parent)
        self.profile = None
        self.profileWidth = 1000
    def onProfileChange(self, p):
        self.profile = p
        self.reload()
    def hasProfile(self):
        return self.profile is not None
    def reload(self):
        self.clear()
        if self.hasProfile():
            self.enableViews.emit()
        else:
            self.disableViews.emit()
            return
        self.profileItm = ProfileItem(None, self, 
                                      QRectF(0, 0, self.profileWidth, 100), 
                                      QPointF(0, 0),
                                      self.profile)
        
