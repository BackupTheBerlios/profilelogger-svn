from DataManagementItemModel import DataManagementItemModel

from PyQt4.QtGui import *

from Model.Brush import Brush
from Gui.ItemModels.BrushItem import BrushItem
from Gui.Dialogs.BrushEditorDialog import BrushEditorDialog

class BrushItemModel(DataManagementItemModel):
    def __init__(self, parent):
        DataManagementItemModel.__init__(self, parent,
                                         Brush,
                                         BrushItem,
                                         BrushEditorDialog,
                                         Brush.name)
        self.headerStrings = [self.tr("Brushes")]
