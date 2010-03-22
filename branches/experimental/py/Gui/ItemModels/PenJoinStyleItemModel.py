from DataSelectionItemModel import DataSelectionItemModel

from PyQt4.QtGui import *

from Model.PenJoinStyle import PenJoinStyle
from Gui.ItemModels.PenJoinStyleItem import PenJoinStyleItem

class PenJoinStyleItemModel(DataSelectionItemModel):
    def __init__(self, parent):
        DataSelectionItemModel.__init__(self, parent,
                                        PenJoinStyle,
                                        PenJoinStyleItem,
                                        PenJoinStyle.name)
        self.headerStrings = [self.tr("Pen Join Styles")]
