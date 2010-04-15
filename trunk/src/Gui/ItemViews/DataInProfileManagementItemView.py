from DataManagementItemView import DataManagementItemView

from PyQt4.QtCore import *
from PyQt4.QtGui import *

class DataInProfileManagementItemView(DataManagementItemView):
    def __init__(self, parent, askForConfirmationBeforeDeleting=False):
        DataManagementItemView.__init__(self, parent, askForConfirmationBeforeDeleting)
        #self.model().enableViews.connect(self.onEnableViews)
        #self.model().disableViews.connect(self.onDisableViews)
        self.setEnabled(False)
    def onEnableViews(self):
        self.setEnabled(True)
    def onDisableViews(self):
        self.setEnabled(False)
