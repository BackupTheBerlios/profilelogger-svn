from ToolBar import *

from Gui.Widgets.FaciesSelectionComboBox import *

from Model.Facies import *

class FaciesToolBar(ToolBar):
    currentFaciesChanged = pyqtSignal(Facies)
    def __init__(self, title, parent):
        ToolBar.__init__(self, title, parent)
        self.project=None
        self.faciesW = FacieselectionComboBox(self)
        self.faciesW.currentDatasetChanged.connect(self.onFaciesChange)
        self.addWidget(QLabel(self.tr("Facies:"), self))
        self.addWidget(self.faciesW)
        self.setEnabled(False)
    def onFaciesChange(self, p):
        self.currentFaciesChanged.emit(p)
    def onProjectChange(self, p):
        self.project = p
        self.faciesW.setProject(p)
        self.setEnabled(self.hasProject())
    def hasProject(self):
        return self.project is not None
    
