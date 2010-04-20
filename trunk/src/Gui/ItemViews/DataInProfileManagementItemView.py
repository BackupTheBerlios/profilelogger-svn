from DataManagementItemView import DataManagementItemView

from PyQt4.QtCore import *
from PyQt4.QtGui import *

class DataInProfileManagementItemView(DataManagementItemView):
    def __init__(self, parent, askForConfirmationBeforeDeleting=False):
        DataManagementItemView.__init__(self, parent, askForConfirmationBeforeDeleting)
        self.setEnabled(False)
    def onEnableViews(self):
        self.setEnabled(True)
    def onDisableViews(self):
        self.setEnabled(False)
    def onProfileChange(self, profile):
        self.model().onProfileChange(profile)
    def setProfile(self, profile):
        self.model().setProfile(profile)
