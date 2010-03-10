from PyQt4.QtGui import *
from PyQt4.QtCore import *

class IdLabel(QLabel):
    def __init__(self, parent):
        QLabel.__init__(self, parent)
    def setValue(self, id):
        if id is None:
            self.setText(self.tr('<Not Set>'))
        else:
            self.setText(QString('%1').arg(id))
