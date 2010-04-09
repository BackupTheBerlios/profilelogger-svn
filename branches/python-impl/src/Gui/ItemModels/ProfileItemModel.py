from DataInProjectManagementItemModel import DataInProjectManagementItemModel

from PyQt4.QtGui import *

from Model.Profile import Profile
from Gui.ItemModels.ProfileItem import ProfileItem
from Gui.Dialogs.ProfileEditorDialog import ProfileEditorDialog

class ProfileItemModel(DataInProjectManagementItemModel):
    def __init__(self, parent):
        DataInProjectManagementItemModel.__init__(self, parent,
                                                  Profile,
                                                  ProfileItem,
                                                  ProfileEditorDialog,
                                                  Profile.name)
        self.headerStrings = [self.tr("Profiles")]
