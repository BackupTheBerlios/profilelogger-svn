from DataManagementItemModel import DataManagementItemModel

from PyQt4.QtGui import *

from Model.Drawing import Drawing
from Gui.ItemModels.DrawingItem import DrawingItem
from Gui.Dialogs.DrawingEditorDialog import DrawingEditorDialog

class DrawingItemModel(DataManagementItemModel):
    def __init__(self, parent):
        DataManagementItemModel.__init__(self, parent,
                                         Drawing,
                                         DrawingItem,
                                         DrawingEditorDialog,
                                         Drawing.name)
        self.headerStrings = [self.tr("Drawings")]
