from DataInProjectManagementItemModel import DataInProjectManagementItemModel

from PyQt4.QtGui import *

from Model.PointOfInterest import PointOfInterest
from Gui.ItemModels.PointOfInterestItem import PointOfInterestItem
from Gui.Dialogs.PointOfInterestEditorDialog import PointOfInterestEditorDialog

class PointOfInterestItemModel(DataInProjectManagementItemModel):
    def __init__(self, parent):
        DataInProjectManagementItemModel.__init__(self, parent,
                                                  PointOfInterest,
                                                  PointOfInterestItem,
                                                  PointOfInterestEditorDialog,
                                                  PointOfInterest.name)
        self.headerStrings = [self.tr("Points Of Interest")]

