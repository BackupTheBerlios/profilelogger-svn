from DataManagementItemModel import DataManagementItemModel

from PyQt4.QtGui import *

from Model.ProfileColumn import ProfileColumn
from Gui.ItemModels.ProfileColumnItem import ProfileColumnItem
from Gui.Dialogs.ProfileColumnEditorDialog import ProfileColumnEditorDialog

class ProfileColumnItemModel(DataManagementItemModel):
    def __init__(self, parent):
        DataManagementItemModel.__init__(self, parent,
                                         ProfileColumn,
                                         ProfileColumnItem,
                                         ProfileColumnEditorDialog,
                                         ProfileColumn.name)
        self.headerStrings = [self.tr("Profile Columns")]
    def setProfile(self, profile):
        pass
