from ManagementItemModel import ManagementItemModel

from PyQt4.QtGui import *

from Logic.Model.FieldBook import FieldBook
from Gui.Dialogs.FieldBookEditorDialog import FieldBookEditorDialog
from ManagmentItemModel import *

class FieldBookItem(StandardItem):
    def __init__(self, entity):
        StandardItem.__init__(self, entity)
        self.showData()

class FieldBookItemModel(ManagementItemModel):
    def __init__(self, parent):
        ManagementItemModel.__init__(self, parent,
                                     FieldBook,
                                     FieldBookItem,
                                     FieldBookEditorDialog,
                                     FieldBookFinder)
        self.headerStrings = [self.tr('Field Books')]
