from PyQt4.QtGui import *
from PyQt4.QtCore import *

class NameEdit(QLineEdit):
    nameChanged = pyqtSignal(QString)

    def __init__(self, parent):
        QLineEdit.__init__(self, parent)
        self.textChanged.connect(self.onTextChange)
    def onTextChange(self, txt):
        self.nameChanged.emit(unicode(txt))
    def setValue(self, txt):
        if txt is not None:
            self.setText(unicode(txt))
        else:
            self.clear()
