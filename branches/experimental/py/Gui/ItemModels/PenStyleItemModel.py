from DataSelectionItemModel import DataSelectionItemModel

from PyQt4.QtGui import *

from Model.PenStyle import PenStyle
from Gui.ItemModels.PenStyleItem import PenStyleItem

class PenStyleItemModel(DataSelectionItemModel):
    def __init__(self, parent):
        DataSelectionItemModel.__init__(self, parent,
                                        PenStyle,
                                        PenStyleItem,
                                        PenStyle.name)
        self.headerStrings = [self.tr("Pen Styles")]
