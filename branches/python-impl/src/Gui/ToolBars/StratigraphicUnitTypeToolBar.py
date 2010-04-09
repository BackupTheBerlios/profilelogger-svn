from ToolBar import *

from Gui.Widgets.StratigraphicUnitTypeSelectionComboBox import *

from Model.StratigraphicUnitType import *

class StratigraphicUnitTypeToolBar(ToolBar):
    currentStratigraphicUnitTypeChanged = pyqtSignal(StratigraphicUnitType)
    def __init__(self, title, parent):
        ToolBar.__init__(self, title, parent)
        self.stratigraphicUnitTypesW = StratigraphicUnitTypeSelectionComboBox(self)
        self.stratigraphicUnitTypesW.currentDatasetChanged.connect(self.onStratigraphicUnitTypeChange)
        self.addWidget(QLabel(self.tr("Stratigraphic Unit Types:"), self))
        self.addWidget(self.stratigraphicUnitTypesW)
    def onStratigraphicUnitTypeChange(self, p):
        self.currentStratigraphicUnitTypeChanged.emit(p)
