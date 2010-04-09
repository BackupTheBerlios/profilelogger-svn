from ToolBar import *

from Gui.Widgets.TectonicUnitTypeSelectionComboBox import *

from Model.TectonicUnitType import *

class TectonicUnitTypeToolBar(ToolBar):
    currentTectonicUnitTypeChanged = pyqtSignal(TectonicUnitType)
    def __init__(self, title, parent):
        ToolBar.__init__(self, title, parent)
        self.tectonicUnitTypesW = TectonicUnitTypeSelectionComboBox(self)
        self.tectonicUnitTypesW.currentDatasetChanged.connect(self.onTectonicUnitTypeChange)
        self.addWidget(QLabel(self.tr("Tectonic Unit Types:"), self))
        self.addWidget(self.tectonicUnitTypesW)
    def onTectonicUnitTypeChange(self, p):
        self.currentTectonicUnitTypeChanged.emit(p)
