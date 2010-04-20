from DataInProfileManagementItemView import DataInProfileManagementItemView

from PyQt4.QtCore import *
from PyQt4.QtGui import *

from Gui.ItemModels.BedItemModel import *

class BedItemView(DataInProfileManagementItemView):
    def __init__(self, parent):
        DataInProfileManagementItemView.__init__(self, parent)
        self.configureModel(BedItemModel(self))
    def setProfile(self, profile):
        self.onProfileChange(profile)
