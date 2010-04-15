from DataInBedManagementItemView import DataInBedManagementItemView

from PyQt4.QtCore import *
from PyQt4.QtGui import *

from Gui.ItemModels.SedimentStructureInBedItemModel import *

class SedimentStructureInBedItemView(DataInBedManagementItemView):
    def __init__(self, parent):
        DataInBedManagementItemView.__init__(self, parent)
        self.configureModel(SedimentStructureInBedItemModel(self))
