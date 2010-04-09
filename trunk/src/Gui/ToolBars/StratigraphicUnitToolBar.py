from ToolBar import *

from Gui.Widgets.StratigraphicUnitSelectionComboBox import *

from Model.StratigraphicUnit import *

class StratigraphicUnitToolBar(ToolBar):
    currentStratigraphicUnitChanged = pyqtSignal(StratigraphicUnit)
    def __init__(self, title, parent):
        ToolBar.__init__(self, title, parent)
        self.project=None
        self.stratigraphicUnitsW = StratigraphicUnitSelectionComboBox(self)
        self.stratigraphicUnitsW.currentDatasetChanged.connect(self.onStratigraphicUnitChange)
        self.addWidget(QLabel(self.tr("StratigraphicUnits:"), self))
        self.addWidget(self.stratigraphicUnitsW)
        self.setEnabled(False)
    def onStratigraphicUnitChange(self, p):
        self.currentStratigraphicUnitChanged.emit(p)
    def onProjectChange(self, p):
        self.project = p
        self.stratigraphicUnitsW.setProject(p)
        self.setEnabled(self.hasProject())
    def hasProject(self):
        return self.project is not None
    
