from ToolBar import *

from Gui.Widgets.BeddingTypeSelectionComboBox import *

from Model.BeddingType import *

class BeddingTypeToolBar(ToolBar):
    currentBeddingTypeChanged = pyqtSignal(BeddingType)
    def __init__(self, title, parent):
        ToolBar.__init__(self, title, parent)
        self.project=None
        self.beddingTypesW = BeddingTypeSelectionComboBox(self)
        self.beddingTypesW.currentDatasetChanged.connect(self.onBeddingTypeChange)
        self.addWidget(QLabel(self.tr("BeddingTypes:"), self))
        self.addWidget(self.beddingTypesW)
        self.setEnabled(False)
    def onBeddingTypeChange(self, p):
        self.currentBeddingTypeChanged.emit(p)
    def onProjectChange(self, p):
        self.project = p
        self.beddingTypesW.setProject(p)
        self.setEnabled(self.hasProject())
    def hasProject(self):
        return self.project is not None
    
