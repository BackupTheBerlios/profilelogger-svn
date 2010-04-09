from ToolBar import *

from Gui.Widgets.SedimentStructureSelectionComboBox import *

from Model.SedimentStructure import *

class SedimentStructureToolBar(ToolBar):
    currentSedimentStructureChanged = pyqtSignal(SedimentStructure)
    def __init__(self, title, parent):
        ToolBar.__init__(self, title, parent)
        self.project=None
        self.sedimentStructuresW = SedimentStructureSelectionComboBox(self)
        self.sedimentStructuresW.currentDatasetChanged.connect(self.onSedimentStructureChange)
        self.addWidget(QLabel(self.tr("Sediment Structures:"), self))
        self.addWidget(self.sedimentStructuresW)
        self.setEnabled(False)
    def onSedimentStructureChange(self, p):
        self.currentSedimentStructureChanged.emit(p)
    def onProjectChange(self, p):
        self.project = p
        self.sedimentStructuresW.setProject(p)
        self.setEnabled(self.hasProject())
    def hasProject(self):
        return self.project is not None
    
