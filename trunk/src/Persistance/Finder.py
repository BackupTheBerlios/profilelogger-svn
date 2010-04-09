from PyQt4.QtCore import *
from PyQt4.QtGui import *

class Finder(QObject):
    def __init__(self, parent):
        pass
    def getSession(self):
        return QApplication.instance().db.session
    def doFindAll(self, dataClass, orderCol):
        return self.getSession().query(dataClass).order_by(orderCol).all()
    def doFindAllInProject(self, dataClass, orderCol, project):
        if project is None:
            return None
        return self.getSession().query(dataClass).order_by(orderCol).filter(dataClass.project == project).all()
