from ToolBar import *

from Gui.Widgets.LengthUnitSelectionComboBox import *

from Model.LengthUnit import *

class LengthUnitToolBar(ToolBar):
    currentLengthUnitChanged = pyqtSignal(LengthUnit)
    def __init__(self, title, parent):
        ToolBar.__init__(self, title, parent)
        self.lengthUnitsW = LengthUnitSelectionComboBox(self)
        self.lengthUnitsW.currentDatasetChanged.connect(self.onLengthUnitChange)
        self.addWidget(QLabel(self.tr("Length Units:"), self))
        self.addWidget(self.lengthUnitsW)
    def onLengthUnitChange(self, p):
        self.currentLengthUnitChanged.emit(p)
