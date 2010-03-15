from DataInProfileAssemblyManagementItemModel import DataInProfileAssemblyManagementItemModel

from PyQt4.QtGui import *

from Model.ProfileInProfileAssembly import ProfileInProfileAssembly
from Gui.ItemModels.ProfileInProfileAssemblyItem import ProfileInProfileAssemblyItem
from Gui.Dialogs.ProfileInProfileAssemblyEditorDialog import ProfileInProfileAssemblyEditorDialog

class ProfileInProfileAssemblyItemModel(DataInProfileAssemblyManagementItemModel):
    def __init__(self, parent):
        DataInProfileAssemblyManagementItemModel.__init__(self, parent,
                                                          ProfileInProfileAssembly,
                                                          ProfileInProfileAssemblyItem,
                                                          ProfileInProfileAssemblyEditorDialog,
                                                          ProfileInProfileAssembly.name)
        self.headerStrings = [self.tr("Profiles In Profile Assembly")]
