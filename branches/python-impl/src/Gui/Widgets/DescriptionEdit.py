from PyQt4.QtGui import *
from PyQt4.QtCore import *

class DescriptionEdit(QTextEdit):
    descriptionChanged = pyqtSignal(QString)

    def __init__(self, parent):
        QLineEdit.__init__(self, parent)
        self.textChanged.connect(self.onTextChanged)
    def onTextChanged(self):
        self.descriptionChanged.emit(unicode(self.toPlainText()))
    def setValue(self, txt):
        self.setPlainText(unicode(txt))
