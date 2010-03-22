from DataManagementItemModel import DataManagementItemModel

from PyQt4.QtGui import *

from Model.Pen import Pen
from Gui.ItemModels.PenItem import PenItem
from Gui.Dialogs.PenEditorDialog import PenEditorDialog

class PenItemModel(DataManagementItemModel):
    def __init__(self, parent):
        DataManagementItemModel.__init__(self, parent,
                                         Pen,
                                         PenItem,
                                         PenEditorDialog,
                                         Pen.name)
        self.headerStrings = [self.tr("Pens")]
