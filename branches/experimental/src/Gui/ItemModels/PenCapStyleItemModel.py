from DataSelectionItemModel import DataSelectionItemModel

from PyQt4.QtGui import *

from Model.PenCapStyle import PenCapStyle
from Gui.ItemModels.PenCapStyleItem import PenCapStyleItem

class PenCapStyleItemModel(DataSelectionItemModel):
    def __init__(self, parent):
        DataSelectionItemModel.__init__(self, parent,
                                        PenCapStyle,
                                        PenCapStyleItem,
                                        PenCapStyle.name)
        self.headerStrings = [self.tr("Pen Cap Styles")]
