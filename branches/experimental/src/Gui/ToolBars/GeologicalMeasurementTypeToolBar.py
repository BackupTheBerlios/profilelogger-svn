from ToolBar import *

from Gui.Widgets.GeologicalMeasurementTypeSelectionComboBox import *

from Model.GeologicalMeasurementType import *

class GeologicalMeasurementTypeToolBar(ToolBar):
    currentGeologicalMeasurementTypeChanged = pyqtSignal(GeologicalMeasurementType)
    def __init__(self, title, parent):
        ToolBar.__init__(self, title, parent)
        self.geologicalMeasurementTypesW = GeologicalMeasurementTypeSelectionComboBox(self)
        self.geologicalMeasurementTypesW.currentDatasetChanged.connect(self.onGeologicalMeasurementTypeChange)
        self.addWidget(QLabel(self.tr("Geological Measurement Types:"), self))
        self.addWidget(self.geologicalMeasurementTypesW)
    def onGeologicalMeasurementTypeChange(self, p):
        self.currentGeologicalMeasurementTypeChanged.emit(p)
