from InProfileItemModel import *

from PyQt4.QtGui import *

from Model.ProfileColumn import ProfileColumn
from Gui.Dialogs.ProfileColumnEditorDialog import ProfileColumnEditorDialog

class ProfileColumnItem(StandardItem):
    def __init__(self, entity):
        StandardItem.__init__(self, entity)
        self.showData()

class ProfileColumnItemModel(InProfileItemModel):
    def __init__(self, parent):
        InProfileItemModel.__init__(self, parent,
                                    ProfileColumn,
                                    ProfileColumnItem,
                                    ProfileColumnEditorDialog,
                                    ProfileColumnFinder)
        self.headerStrings = [self.tr('Profile Columns')]
