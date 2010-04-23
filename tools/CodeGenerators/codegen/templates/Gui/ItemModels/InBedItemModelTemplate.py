from InBedItemModel import *

from PyQt4.QtGui import *

from Model.<class_name> import <class_name>
from Gui.Dialogs.<class_name>EditorDialog import <class_name>EditorDialog

class <class_name>Item(StandardItem):
    def __init__(self, entity):
        StandardItem.__init__(self, entity)
        self.showData()

class <class_name>ItemModel(InBedItemModel):
    def __init__(self, parent):
        InBedItemModel.__init__(self, parent,
                                <class_name>,
                                <class_name>Item,
                                <class_name>EditorDialog,
                                <class_name>Finder)
        self.headerStrings = [<header_strings>]
