from GraphicsScene import *

from PyQt4.QtCore import *

class ProfileScene(GraphicsScene):
    enableViews = pyqtSignal()
    disableViews = pyqtSignal()

    def __init__(self, parent):
        GraphicsScene.__init__(self, parent)
        self.profile = None
        self.disableViews.emit()
    def onProfileChange(self, p):
        self.profile = p
        self.enableViews.emit()
