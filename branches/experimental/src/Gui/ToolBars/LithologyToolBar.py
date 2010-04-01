from ToolBar import *

from Gui.Widgets.LithologySelectionComboBox import *

from Model.Lithology import *

class LithologyToolBar(ToolBar):
    currentLithologyChanged = pyqtSignal(Lithology)
    def __init__(self, title, parent):
        ToolBar.__init__(self, title, parent)
        self.project=None
        self.lithologiesW = LithologySelectionComboBox(self)
        self.lithologiesW.currentDatasetChanged.connect(self.onLithologyChange)
        self.addWidget(QLabel(self.tr("Lithologies:"), self))
        self.addWidget(self.lithologiesW)
        self.setEnabled(False)
    def onLithologyChange(self, p):
        self.currentLithologyChanged.emit(p)
    def onProjectChange(self, p):
        self.project = p
        self.lithologiesW.setProject(p)
        self.setEnabled(self.hasProject())
    def hasProject(self):
        return self.project is not None
    
