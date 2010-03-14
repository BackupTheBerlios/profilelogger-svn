from DataInProjectManagementItemModel import DataInProjectManagementItemModel

from PyQt4.QtGui import *

from Model.ProfileAssembly import ProfileAssembly
from Gui.ItemModels.ProfileAssemblyItem import ProfileAssemblyItem
from Gui.Dialogs.ProfileAssemblyEditorDialog import ProfileAssemblyEditorDialog

class ProfileAssemblyItemModel(DataInProjectManagementItemModel):
    def __init__(self, parent):
        DataInProjectManagementItemModel.__init__(self, parent,
                                                  ProfileAssembly,
                                                  ProfileAssemblyItem,
                                                  ProfileAssemblyEditorDialog,
                                                  ProfileAssembly.name)
        self.headerStrings = [self.tr("Profile Assemblies")]
