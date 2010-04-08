from NamedDescribedDataset import NamedDescribedDataset

class ProfileInProfileAssembly(NamedDescribedDataset):
    def __init__(self, profileAssembly, id=None, name=None, description=None):
        super(ProfileInProfileAssembly, self).__init__(id, name, description)
        self.profileAssembly = profileAssembly

        self.showBigHeightMarks = True
        self.showSmallHeightMarks = True
        self.showBigHeightMarkLabels = True
        self.showSmallHeightMarkLabels = True
        self.showLithology = True
        self.showLithologyNumberInLithology = True
        self.showGrainSize = True
        self.showBeddingTypeInGrainSizeColumn = True
        self.showBeddingTypeInColumn = True
        self.showBeddingTypeNumber = True
        self.showBedNumberInLithology = True
        self.showBedNumberInColumn = True
        self.showBedHeightInLithology = True
        self.showBedHeightInColumn = True
        self.showFossilsInColumn = True
        self.showFossilsInBeddingType = True
        self.showFossilsInLithology = True
        self.showSedimentStructuresInColumn = True
        self.showSedimentStructuresInLithology = True
        self.showSedimentStructuresInBeddingType = True
        self.showCustomSymbolsInColumn = True
        self.showCustomSymbolsInLithology = True
        self.showCustomSymbolsInBeddingType = True
        self.showFaciesInColumn = True
        self.showLithologicalUnitInColumn = True
        self.showTectonicUnitInColumn = True
        self.showStratigraphicUnitInColumn = True
        
        self.bedNumbersColumnWidth = 0
        self.bedHeightsColumnWidth = 0
        self.lithologiesColumnWidth = 0
        self.beddingTypesColumnWidth = 0
        self.grainSizesColumnWidth = 0
        self.fossilsColumnWidth = 0
        self.sedimentStructuresColumnWidth = 0
        self.customSymbolsColumnWidth = 0
        self.faciesColumnWidth = 0
        self.lithologicalUnitsColumnWidth = 0
        self.tectonicUnitsColumnWidth = 0
        self.stratigraphicUnitsColumnWidth = 0

        self.grainSizeTypesInLegend = []

        self.scale = 1.0
        self.bigHeightMarksDistanceValue = 1
        self.bigHeightMarksDistanceLengthUnit = None
        self.smallHeightMarksDistanceValue = 1
        self.smallHeightMarksDistanceLengthUnit = None

        self.firstBedInView = None
        self.lastBedInView = None
