from ToolBar import *

from Gui.Widgets.GrainSizeTypeSelectionComboBox import *

from Model.GrainSizeType import *

class GrainSizeTypeToolBar(ToolBar):
    currentGrainSizeTypeChanged = pyqtSignal(GrainSizeType)
    def __init__(self, title, parent):
        ToolBar.__init__(self, title, parent)
        self.grainSizeTypesW = GrainSizeTypeSelectionComboBox(self)
        self.grainSizeTypesW.currentDatasetChanged.connect(self.onGrainSizeTypeChange)
        self.addWidget(QLabel(self.tr("Grain Size Types:"), self))
        self.addWidget(self.grainSizeTypesW)
    def onGrainSizeTypeChange(self, p):
        self.currentGrainSizeTypeChanged.emit(p)
