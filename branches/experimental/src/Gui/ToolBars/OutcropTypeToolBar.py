from ToolBar import *

from Gui.Widgets.OutcropTypeSelectionComboBox import *

from Model.OutcropType import *

class OutcropTypeToolBar(ToolBar):
    currentOutcropTypeChanged = pyqtSignal(OutcropType)
    def __init__(self, title, parent):
        ToolBar.__init__(self, title, parent)
        self.project=None
        self.outcropTypesW = OutcropTypeSelectionComboBox(self)
        self.outcropTypesW.currentDatasetChanged.connect(self.onOutcropTypeChange)
        self.addWidget(QLabel(self.tr("Outcrop Types:"), self))
        self.addWidget(self.outcropTypesW)
        self.setEnabled(False)
    def onOutcropTypeChange(self, p):
        self.currentOutcropTypeChanged.emit(p)
    def onProjectChange(self, p):
        self.project = p
        self.outcropTypesW.setProject(p)
        self.setEnabled(self.hasProject())
    def hasProject(self):
        return self.project is not None
    
