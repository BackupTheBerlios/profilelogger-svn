from DataInProfileAssemblyManagementItemView import DataInProfileAssemblyManagementItemView

from PyQt4.QtCore import *
from PyQt4.QtGui import *

from Gui.ItemModels.ProfileInProfileAssemblyItemModel import *

class ProfileInProfileAssemblyItemView(DataInProfileAssemblyManagementItemView):
    def __init__(self, parent):
        DataInProfileAssemblyManagementItemView.__init__(self, parent)
        self.configureModel(ProfileInProfileAssemblyItemModel(self))
    def setProfileAssembly(self, assembly):
        self.model().setProfileAssembly(assembly)
