"""
Boilerplate comment
"""

from PyQt4.QtCore import *
from PyQt4.QtGui import *

class Finder(QObject):
    def __init__(self, parent):
        QObject.__init__(self, parent)
    def getSession(self):
        return QApplication.instance().db.session
    def doFindAll(self, dataClass):
        return self.getSession().query(dataClass).all()
