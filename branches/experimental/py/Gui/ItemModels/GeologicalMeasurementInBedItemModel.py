from DataInBedManagementItemModel import DataInBedManagementItemModel

from PyQt4.QtGui import *

from Model.GeologicalMeasurementInBed import GeologicalMeasurementInBed
from Gui.ItemModels.GeologicalMeasurementInBedItem import GeologicalMeasurementInBedItem
from Gui.Dialogs.GeologicalMeasurementInBedEditorDialog import GeologicalMeasurementInBedEditorDialog

class GeologicalMeasurementInBedItemModel(DataInBedManagementItemModel):
    def __init__(self, parent):
        DataInBedManagementItemModel.__init__(self, parent,
                                              GeologicalMeasurementInBed,
                                              GeologicalMeasurementInBedItem,
                                              GeologicalMeasurementInBedEditorDialog,
                                              GeologicalMeasurementInBed.id)
        self.headerStrings = [self.tr("Geological Measurements")]
