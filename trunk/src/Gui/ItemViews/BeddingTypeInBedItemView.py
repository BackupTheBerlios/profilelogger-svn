from DataInBedManagementItemView import DataInBedManagementItemView

from PyQt4.QtCore import *
from PyQt4.QtGui import *
from Gui.ItemModels.BeddingTypeInBedItemModel import *
class BeddingTypeInBedItemView(DataInBedManagementItemView):
    def __init__(self, parent):
        DataInBedManagementItemView.__init__(self, parent)
        self.configureModel(BeddingTypeInBedItemModel(self))
