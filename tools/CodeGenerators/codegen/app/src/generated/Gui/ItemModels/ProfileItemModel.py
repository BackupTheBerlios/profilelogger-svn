from InProjectItemModel import *

from PyQt4.QtGui import *

from Model.Profile import Profile
from Gui.Dialogs.ProfileEditorDialog import ProfileEditorDialog

class ProfileItem(StandardItem):
    def __init__(self, entity):
        StandardItem.__init__(self, entity)
        self.showData()

class ProfileItemModel(InProjectItemModel):
    def __init__(self, parent):
        InProjectItemModel.__init__(self, parent,
                                    Profile,
                                    ProfileItem,
                                    ProfileEditorDialog,
                                    ProfileFinder)
        self.headerStrings = [self.tr('Profiles')]
