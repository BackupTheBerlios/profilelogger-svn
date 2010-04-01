from ToolBar import *

from Gui.Widgets.CustomSymbolSelectionComboBox import *

from Model.CustomSymbol import *

class CustomSymbolToolBar(ToolBar):
    currentCustomSymbolChanged = pyqtSignal(CustomSymbol)
    def __init__(self, title, parent):
        ToolBar.__init__(self, title, parent)
        self.project=None
        self.customSymbolsW = CustomSymbolSelectionComboBox(self)
        self.customSymbolsW.currentDatasetChanged.connect(self.onCustomSymbolChange)
        self.addWidget(QLabel(self.tr("Custom Symbols:"), self))
        self.addWidget(self.customSymbolsW)
        self.setEnabled(False)
    def onCustomSymbolChange(self, p):
        self.currentCustomSymbolChanged.emit(p)
    def onProjectChange(self, p):
        self.project = p
        self.customSymbolsW.setProject(p)
        self.setEnabled(self.hasProject())
    def hasProject(self):
        return self.project is not None
    
