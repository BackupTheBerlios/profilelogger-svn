from ToolBar import *

from Gui.Widgets.GrainSizeTypeSelectionComboBox import *
from Gui.Widgets.GrainSizeSelectionComboBox import *
from Gui.Widgets.LengthUnitSelectionComboBox import *
from Gui.Widgets.SvgItemSelectionComboBox import *
from Gui.Widgets.GeologicalMeasurementTypeSelectionComboBox import *
from Gui.Widgets.LithologicalUnitTypeSelectionComboBox import *
from Gui.Widgets.TectonicUnitTypeSelectionComboBox import *
from Gui.Widgets.StratigraphicUnitTypeSelectionComboBox import *
from Gui.Widgets.ProfileColumnSelectionComboBox import *

class GlobalToolsToolBar(ToolBar):
    def __init__(self, title, parent):
        ToolBar.__init__(self, title, parent)

        self.grainSizeTypesW = GrainSizeTypeSelectionComboBox(self)
        self.grainSizesW = GrainSizeSelectionComboBox(self)
        self.lengthUnitsW = LengthUnitSelectionComboBox(self)
        self.svgItemsW = SvgItemSelectionComboBox(self)
        self.geologicalMeasurementTypesW = GeologicalMeasurementTypeSelectionComboBox(self)
        self.lithologicalUnitTypesW = LithologicalUnitTypeSelectionComboBox(self)
        self.tectonicUnitTypesW = TectonicUnitTypeSelectionComboBox(self)
        self.stratigraphicUnitTypesW = StratigraphicUnitTypeSelectionComboBox(self)
        self.profileColumnsW = ProfileColumnSelectionComboBox(self)

        self.addWidget(self.grainSizeTypesW)
        self.addWidget(self.grainSizesW)
        self.addWidget(self.lengthUnitsW)
        self.addWidget(self.svgItemsW)
        self.addWidget(self.geologicalMeasurementTypesW)
        self.addWidget(self.lithologicalUnitTypesW)
        self.addWidget(self.tectonicUnitTypesW)
        self.addWidget(self.stratigraphicUnitTypesW)
        self.addWidget(self.profileColumnsW)

