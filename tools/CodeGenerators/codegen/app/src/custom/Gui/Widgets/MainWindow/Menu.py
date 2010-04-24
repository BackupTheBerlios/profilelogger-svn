from PyQt4.QtGui import *
from PyQt4.QtCore import *

class Menu(QMenu):
    def __init__(self, title, parent, actions=[]):
        QMenu.__init__(self, title, parent)
        for a in actions:
            if a is not None:
                self.addAction(a)
            else:
                self.addSeparator()
