from InFieldBookItemModel import *

from PyQt4.QtGui import *

from Model.FieldBookEntry import FieldBookEntry
from Gui.Dialogs.FieldBookEntryEditorDialog import FieldBookEntryEditorDialog

class FieldBookEntryItem(StandardItem):
    def __init__(self, entity):
        StandardItem.__init__(self, entity)
        self.showData()

class FieldBookEntryItemModel(InFieldBookItemModel):
    def __init__(self, parent):
        InFieldBookItemModel.__init__(self, parent,
                                      FieldBookEntry,
                                      FieldBookEntryItem,
                                      FieldBookEntryEditorDialog,
                                      FieldBookEntryFinder)
        self.headerStrings = [self.tr('Field Book Entry')]
