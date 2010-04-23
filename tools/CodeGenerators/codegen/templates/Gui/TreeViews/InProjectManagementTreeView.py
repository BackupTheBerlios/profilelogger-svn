from ManagementTreeView import ManagementTreeView

from PyQt4.QtCore import *
from PyQt4.QtGui import *

class InProjectManagementTreeView(DataManagementTreeView):
    def __init__(self, parent):
        DataManagementTreeView.__init__(self, parent)
        self.setEnabled(False)
    def onEnableViews(self):
        self.setEnabled(True)
    def onDisableViews(self):
        self.setEnabled(False)
    def setProject(self, project):
        self.model().setProject(project)
