from DataInProjectManagementItemModel import DataInProjectManagementItemModel

from PyQt4.QtGui import *

from Model.Color import Color
from Gui.ItemModels.ColorItem import ColorItem
from Gui.Dialogs.ColorEditorDialog import ColorEditorDialog

class ColorItemModel(DataInProjectManagementItemModel):
    def __init__(self, parent):
        DataInProjectManagementItemModel.__init__(self, parent,
                                                  Color,
                                                  ColorItem,
                                                  ColorEditorDialog,
                                                  Color.name)
        self.headerStrings = [self.tr("Colors")]
