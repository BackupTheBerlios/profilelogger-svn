from ToolBar import *

from Gui.Widgets.ProjectSelectionComboBox import *
from Gui.Widgets.LithologySelectionComboBox import *
from Gui.Widgets.ColorSelectionComboBox import *
from Gui.Widgets.ProfileSelectionComboBox import *
from Gui.Widgets.ProfileAssemblySelectionComboBox import *
from Gui.Widgets.PointOfInterestSelectionComboBox import *
from Gui.Widgets.SedimentStructureSelectionComboBox import *
from Gui.Widgets.OutcropTypeSelectionComboBox import *
from Gui.Widgets.FaciesSelectionComboBox import *
from Gui.Widgets.LithologicalUnitSelectionComboBox import *
from Gui.Widgets.StratigraphicUnitSelectionComboBox import *
from Gui.Widgets.TectonicUnitSelectionComboBox import *
from Gui.Widgets.BeddingTypeSelectionComboBox import *
from Gui.Widgets.FossilSelectionComboBox import *
from Gui.Widgets.CustomSymbolSelectionComboBox import *
from Gui.Widgets.BoundaryTypeSelectionComboBox import *

class ProjectToolsToolBar(ToolBar):
    def __init__(self, title, parent):
        ToolBar.__init__(self, title, parent)

        self.projectsW = ProjectSelectionComboBox(self)
        self.profilesW = ProfileSelectionComboBox(self)
        self.profileAssembliesW = ProfileAssemblySelectionComboBox(self)
        self.lithologiesW = LithologySelectionComboBox(self)
        self.pointOfInterestsW = PointOfInterestSelectionComboBox(self)
        self.sedimentStructuresW = SedimentStructureSelectionComboBox(self)
        self.fossilsW = FossilSelectionComboBox(self)
        self.customSymbolsW = CustomSymbolSelectionComboBox(self)
        self.colorsW = ColorSelectionComboBox(self)
        self.outcropTypesW = OutcropTypeSelectionComboBox(self)
        self.faciesW = FaciesSelectionComboBox(self)
        self.lithologicalUnitsW = LithologicalUnitSelectionComboBox(self)
        self.stratigraphicUnitsW = StratigraphicUnitSelectionComboBox(self)
        self.tectonicUnitsW = TectonicUnitSelectionComboBox(self)
        self.beddingTypesW = BeddingTypeSelectionComboBox(self)
        self.boundaryTypesW = BoundaryTypeSelectionComboBox(self)

        self.projectsW.currentDatasetChanged.connect(self.lithologiesW.onProjectChange)
        self.projectsW.currentDatasetChanged.connect(self.colorsW.onProjectChange)
        self.projectsW.currentDatasetChanged.connect(self.profilesW.onProjectChange)
        self.projectsW.currentDatasetChanged.connect(self.profileAssembliesW.onProjectChange)
        self.projectsW.currentDatasetChanged.connect(self.pointOfInterestsW.onProjectChange)
        self.projectsW.currentDatasetChanged.connect(self.sedimentStructuresW.onProjectChange)
        self.projectsW.currentDatasetChanged.connect(self.fossilsW.onProjectChange)
        self.projectsW.currentDatasetChanged.connect(self.customSymbolsW.onProjectChange)
        self.projectsW.currentDatasetChanged.connect(self.outcropTypesW.onProjectChange)
        self.projectsW.currentDatasetChanged.connect(self.faciesW.onProjectChange)
        self.projectsW.currentDatasetChanged.connect(self.lithologicalUnitsW.onProjectChange)
        self.projectsW.currentDatasetChanged.connect(self.stratigraphicUnitsW.onProjectChange)
        self.projectsW.currentDatasetChanged.connect(self.tectonicUnitsW.onProjectChange)
        self.projectsW.currentDatasetChanged.connect(self.beddingTypesW.onProjectChange)
        self.projectsW.currentDatasetChanged.connect(self.boundaryTypesW.onProjectChange)

        self.addWidget(self.projectsW)
        self.addWidget(self.profilesW)
        self.addWidget(self.profileAssembliesW)
        self.addWidget(self.lithologiesW)
        self.addWidget(self.sedimentStructuresW)
        self.addWidget(self.fossilsW)
        self.addWidget(self.customSymbolsW)
        self.addWidget(self.colorsW)
        self.addWidget(self.outcropTypesW)
        self.addWidget(self.faciesW)
        self.addWidget(self.lithologicalUnitsW)
        self.addWidget(self.tectonicUnitsW)
        self.addWidget(self.stratigraphicUnitsW)
        self.addWidget(self.beddingTypesW)
        self.addWidget(self.boundaryTypesW)
        self.addWidget(self.pointOfInterestsW)
