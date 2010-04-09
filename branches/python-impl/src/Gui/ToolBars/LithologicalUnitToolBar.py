from ToolBar import *

from Gui.Widgets.LithologicalUnitSelectionComboBox import *

from Model.LithologicalUnit import *

class LithologicalUnitToolBar(ToolBar):
    currentLithologicalUnitChanged = pyqtSignal(LithologicalUnit)
    def __init__(self, title, parent):
        ToolBar.__init__(self, title, parent)
        self.project=None
        self.lithologicalUnitsW = LithologicalUnitSelectionComboBox(self)
        self.lithologicalUnitsW.currentDatasetChanged.connect(self.onLithologicalUnitChange)
        self.addWidget(QLabel(self.tr("LithologicalUnits:"), self))
        self.addWidget(self.lithologicalUnitsW)
        self.setEnabled(False)
    def onLithologicalUnitChange(self, p):
        self.currentLithologicalUnitChanged.emit(p)
    def onProjectChange(self, p):
        self.project = p
        self.lithologicalUnitsW.setProject(p)
        self.setEnabled(self.hasProject())
    def hasProject(self):
        return self.project is not None
    
