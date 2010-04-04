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
    def contextMenuEvent(self, e):
        m = QMenu(self)

        reloadA = QAction(self.tr("Reload"), self)
        m.addAction(reloadA)
        reloadA.triggered.connect(self.scene().reload)

        m.exec_(self.mapToGlobal(e.pos()))
        
