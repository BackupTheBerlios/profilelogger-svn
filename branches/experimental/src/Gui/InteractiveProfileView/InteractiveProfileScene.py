from PyQt4.QtCore import *
from PyQt4.QtGui import *

class InteractiveProfileScene(QGraphicsScene):
    enableViews = pyqtSignal()
    disableViews = pyqtSignal()
    def __init__(self, parent):
        QGraphicsScene.__init__(self, parent)
        self.profile = None
    def onProfileChange(self, p):
        self.profile = p
        self.reload()
    def hasProfile(self):
        return self.profile is not None
    def reload(self):
        if self.hasProfile():
            self.enableViews.emit()
        else:
            self.disableViews.emit()
            return
