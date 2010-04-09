from DataSelectionComboBox import DataSelectionComboBox

from Gui.ManagementDialogs.GeologicalMeasurementTypeManagementDialog import *
from Persistance.GeologicalMeasurementTypeFinder import *

class GeologicalMeasurementTypeSelectionComboBox(DataSelectionComboBox):
    def __init__(self, parent):
        DataSelectionComboBox.__init__(self, parent, 
                                       GeologicalMeasurementTypeManagementDialog,
                                       GeologicalMeasurementTypeFinder)
        self.setToolTip(self.tr("Geological Measurement Types"))
