from ToolBar import *

from Gui.Widgets.BoundaryTypeSelectionComboBox import *

from Model.BoundaryType import *

class BoundaryTypeToolBar(ToolBar):
    currentBoundaryTypeChanged = pyqtSignal(BoundaryType)
    def __init__(self, title, parent):
        ToolBar.__init__(self, title, parent)
        self.project=None
        self.boundaryTypesW = BoundaryTypeSelectionComboBox(self)
        self.boundaryTypesW.currentDatasetChanged.connect(self.onBoundaryTypeChange)
        self.addWidget(QLabel(self.tr("Boundary Types:"), self))
        self.addWidget(self.boundaryTypesW)
        self.setEnabled(False)
    def onBoundaryTypeChange(self, p):
        self.currentBoundaryTypeChanged.emit(p)
    def onProjectChange(self, p):
        self.project = p
        self.boundaryTypesW.setProject(p)
        self.setEnabled(self.hasProject())
    def hasProject(self):
        return self.project is not None
    
