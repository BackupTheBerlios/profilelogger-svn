from ToolBar import *

from Gui.Widgets.GrainSizeSelectionComboBox import *

from Model.GrainSize import *

class GrainSizeToolBar(ToolBar):
    currentGrainSizeChanged = pyqtSignal(GrainSize)
    def __init__(self, title, parent):
        ToolBar.__init__(self, title, parent)
        self.grainSizesW = GrainSizeSelectionComboBox(self)
        self.grainSizesW.currentDatasetChanged.connect(self.onGrainSizeChange)
        self.addWidget(QLabel(self.tr("Grain Sizes:"), self))
        self.addWidget(self.grainSizesW)
    def onGrainSizeChange(self, p):
        self.currentGrainSizeChanged.emit(p)
