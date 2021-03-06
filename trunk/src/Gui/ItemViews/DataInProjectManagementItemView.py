from DataManagementItemView import DataManagementItemView

from PyQt4.QtCore import *
from PyQt4.QtGui import *

class DataInProjectManagementItemView(DataManagementItemView):
    def __init__(self, parent):
        DataManagementItemView.__init__(self, parent)
        #self.model().enableViews.connect(self.onEnableViews)
        #self.model().disableViews.connect(self.onDisableViews)
        self.setEnabled(False)
    def onEnableViews(self):
        self.setEnabled(True)
    def onDisableViews(self):
        self.setEnabled(False)
    def setProject(self, project):
        self.model().setProject(project)
