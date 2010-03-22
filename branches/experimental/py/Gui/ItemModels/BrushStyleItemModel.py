from DataSelectionItemModel import DataSelectionItemModel

from PyQt4.QtGui import *

from Model.BrushStyle import BrushStyle
from Gui.ItemModels.BrushStyleItem import BrushStyleItem

class BrushStyleItemModel(DataSelectionItemModel):
    def __init__(self, parent):
        DataSelectionItemModel.__init__(self, parent,
                                        BrushStyle,
                                        BrushStyleItem,
                                        BrushStyle.name)
        self.headerStrings = [self.tr("Brush Styles")]
