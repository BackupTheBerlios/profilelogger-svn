from InProfileItemModel import *

from PyQt4.QtGui import *

from Model.ProfileColumnInProfile import ProfileColumnInProfile
from Gui.Dialogs.ProfileColumnInProfileEditorDialog import ProfileColumnInProfileEditorDialog

class ProfileColumnInProfileItem(StandardItem):
    def __init__(self, entity):
        StandardItem.__init__(self, entity)
        self.showData()

class ProfileColumnInProfileItemModel(InProfileItemModel):
    def __init__(self, parent):
        InProfileItemModel.__init__(self, parent,
                                    ProfileColumnInProfile,
                                    ProfileColumnInProfileItem,
                                    ProfileColumnInProfileEditorDialog,
                                    ProfileColumnInProfileFinder)
        self.headerStrings = [self.tr('Profile Column In Profile')]
