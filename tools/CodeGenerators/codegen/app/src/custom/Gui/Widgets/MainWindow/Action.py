from PyQt4.QtCore import *
from PyQt4.QtGui import *

class Action(QAction):
    def __init__(self, title, parent, slot=None, shortcut=None):
        QAction.__init__(self, title, parent)
        if slot is not None:
            self.triggered.connect(slot)
        if shortcut is not None:
            self.setShortcut(shortcut)
