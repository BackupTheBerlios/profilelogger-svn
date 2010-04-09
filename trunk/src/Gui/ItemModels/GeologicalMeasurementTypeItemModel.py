from DataManagementItemModel import DataManagementItemModel

from PyQt4.QtGui import *

from Model.GeologicalMeasurementType import GeologicalMeasurementType
from Gui.ItemModels.GeologicalMeasurementTypeItem import GeologicalMeasurementTypeItem
from Gui.Dialogs.GeologicalMeasurementTypeEditorDialog import GeologicalMeasurementTypeEditorDialog

class GeologicalMeasurementTypeItemModel(DataManagementItemModel):
    def __init__(self, parent):
        DataManagementItemModel.__init__(self, parent,
                                         GeologicalMeasurementType,
                                         GeologicalMeasurementTypeItem,
                                         GeologicalMeasurementTypeEditorDialog,
                                         GeologicalMeasurementType.name)
        self.headerStrings = [self.tr("Geological Measurement Types")]
