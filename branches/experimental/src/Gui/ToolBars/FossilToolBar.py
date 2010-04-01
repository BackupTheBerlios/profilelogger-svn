from ToolBar import *

from Gui.Widgets.FossilSelectionComboBox import *

from Model.Fossil import *

class FossilToolBar(ToolBar):
    currentFossilChanged = pyqtSignal(Fossil)
    def __init__(self, title, parent):
        ToolBar.__init__(self, title, parent)
        self.project=None
        self.fossilsW = FossilSelectionComboBox(self)
        self.fossilsW.currentDatasetChanged.connect(self.onFossilChange)
        self.addWidget(QLabel(self.tr("Fossils:"), self))
        self.addWidget(self.fossilsW)
        self.setEnabled(False)
    def onFossilChange(self, p):
        self.currentFossilChanged.emit(p)
    def onProjectChange(self, p):
        self.project = p
        self.fossilsW.setProject(p)
        self.setEnabled(self.hasProject())
    def hasProject(self):
        return self.project is not None
    
