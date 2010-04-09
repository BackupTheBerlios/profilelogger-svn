from DataManagementItemModel import DataManagementItemModel

from PyQt4.QtGui import *

from Model.SVGItem import SVGItem
from Gui.ItemModels.SVGItemItem import SVGItemItem
from Gui.Dialogs.SVGItemEditorDialog import SVGItemEditorDialog

class SVGItemModel(DataManagementItemModel):
    def __init__(self, parent):
        DataManagementItemModel.__init__(self, parent,
                                         SVGItem,
                                         SVGItemItem,
                                         SVGItemEditorDialog,
                                         SVGItem.name)
        self.headerStrings = [self.tr("SVG Items")]
