from PyQt4.QtGui import *

class StandardItem(QStandardItem):
    def __init__(self, data):
        QStandardItem.__init__(self)
        self.data = data
        self.setText(unicode(self.data.name))
        self.setToolTip(unicode(self.data.makeToolTip()))
