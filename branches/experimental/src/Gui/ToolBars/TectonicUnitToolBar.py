from ToolBar import *

from Gui.Widgets.TectonicUnitSelectionComboBox import *

from Model.TectonicUnit import *

class TectonicUnitToolBar(ToolBar):
    currentTectonicUnitChanged = pyqtSignal(TectonicUnit)
    def __init__(self, title, parent):
        ToolBar.__init__(self, title, parent)
        self.project=None
        self.tectonicUnitsW = TectonicUnitSelectionComboBox(self)
        self.tectonicUnitsW.currentDatasetChanged.connect(self.onTectonicUnitChange)
        self.addWidget(QLabel(self.tr("TectonicUnits:"), self))
        self.addWidget(self.tectonicUnitsW)
        self.setEnabled(False)
    def onTectonicUnitChange(self, p):
        self.currentTectonicUnitChanged.emit(p)
    def onProjectChange(self, p):
        self.project = p
        self.tectonicUnitsW.setProject(p)
        self.setEnabled(self.hasProject())
    def hasProject(self):
        return self.project is not None
    
