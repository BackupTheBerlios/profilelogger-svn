from ToolBar import *

from Gui.Widgets.ColorSelectionComboBox import *

from Model.Color import *

class ColorToolBar(ToolBar):
    currentColorChanged = pyqtSignal(Color)
    def __init__(self, title, parent):
        ToolBar.__init__(self, title, parent)
        self.project=None
        self.colorsW = ColorSelectionComboBox(self)
        self.colorsW.currentDatasetChanged.connect(self.onColorChange)
        self.addWidget(QLabel(self.tr("Colors:"), self))
        self.addWidget(self.colorsW)
        self.setEnabled(False)
    def onColorChange(self, p):
        self.currentColorChanged.emit(p)
    def onProjectChange(self, p):
        self.project = p
        self.colorsW.setProject(p)
        self.setEnabled(self.hasProject())
    def hasProject(self):
        return self.project is not None
    
