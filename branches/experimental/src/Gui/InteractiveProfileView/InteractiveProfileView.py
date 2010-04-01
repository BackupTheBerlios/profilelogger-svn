from PyQt4.QtGui import *
from PyQt4.QtCore import *

class InteractiveProfileView(QGraphicsView):
    def __init__(self, parent, modelClass):
        QGraphicsView.__init__(self, parent)
        self.setScene(modelClass(self))
        self.scene().enableViews.connect(self.onEnableMe)
        self.scene().disableViews.connect(self.onDisableMe)
    def onDisableMe(self):
        self.setEnabled(False)
    def onEnableMe(self):
        self.setEnabled(True)
