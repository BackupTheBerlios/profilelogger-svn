from GraphicsScene import *

from PyQt4.QtCore import *

from ProfileItem import ProfileItem

class ProfileScene(GraphicsScene):
    enableViews = pyqtSignal()
    disableViews = pyqtSignal()

    def __init__(self, parent):
        GraphicsScene.__init__(self, parent)
        self.profile = None
        self.disableViews.emit()
    def hasProfile(self):
        return self.profile is not None
    def onProfileChange(self, p):
        self.clear()
        self.profile = p
        if not self.hasProfile():
            return
        self.profileItem = ProfileItem(None, self, self.profile)
        self.enableViews.emit()
