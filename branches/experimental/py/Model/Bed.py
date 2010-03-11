from NamedDescribedDataset import NamedDescribedDataset

class Bed(NamedDescribedDataset):
    def __init__(self, profile, id=None, 
                 height=0, lengthUnit=None,
                 number=0,
                 name=None, description=None):
        super(Bed, self).__init__(id, name, description)
        self.height = height
        self.lengthUnit = lengthUnit
        self.profile = profile
        self.number = number

        self.lithologies = []
        self.colors = []
        self.beddingTypes = []
        self.customSymbols = []
        self.sedimentStructures = []
        self.fossils = []
        self.customSymbols = []
        self.grainSizes = []

        self.topBoundaryType = None
        self.poi = None
        
        self.profile.registerBed(self)
    def hasNumber(self):
        return self.number is not None
    def hasLithology(self):
        return len(self.lithologies) > 0
    def hasColor(self):
        return len(self.colors) > 0
    def hasBeddingType(self):
        return len(self.beddingTypes) > 0
    def hasTopBoundaryType(self):
        return self.topBoundaryType is not None
    def hasPoi(self):
        return self.poi is not None
    def hasBaseGrainSize(self):
        return self.baseGrainSize is not None
    def hasTopGrainSize(self):
        return self.topGrainSize is not None
    def hasCustomSymbol(self):
        return len(self.customSymbols) > 0
    def registerLithology(self, l):
        self.lithologies.append(l)
    def registerColor(self, c):
        self.colors.append(c)
    def registerBeddingType(self, t):
        self.beddingTypes.append(t)
    def registerCustomSymbol(self, t):
        self.customSymbols.append(t)
    def registerSedimentStructure(self, s):
        self.sedimentStructures.append(s)
    def registerFossil(self, f):
        self.fossils.append(f)
    def registerGrainSize(self, s):
        self.grainSizes.append(s)
    def __str__(self):
        return self.name
