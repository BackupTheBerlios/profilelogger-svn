from PyQt4.QtGui import *
from PyQt4.QtCore import *

class TreeView(QTreeView):
    def __init__(self, parent):
        QTreeView.__init__(self, parent)
        self.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.setSortingEnabled(True)
