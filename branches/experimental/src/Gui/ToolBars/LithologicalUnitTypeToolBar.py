from ToolBar import *

from Gui.Widgets.LithologicalUnitTypeSelectionComboBox import *

from Model.LithologicalUnitType import *

class LithologicalUnitTypeToolBar(ToolBar):
    currentLithologicalUnitTypeChanged = pyqtSignal(LithologicalUnitType)
    def __init__(self, title, parent):
        ToolBar.__init__(self, title, parent)
        self.lithologicalUnitTypesW = LithologicalUnitTypeSelectionComboBox(self)
        self.lithologicalUnitTypesW.currentDatasetChanged.connect(self.onLithologicalUnitTypeChange)
        self.addWidget(QLabel(self.tr("Lithological Unit Types:"), self))
        self.addWidget(self.lithologicalUnitTypesW)
    def onLithologicalUnitTypeChange(self, p):
        self.currentLithologicalUnitTypeChanged.emit(p)
