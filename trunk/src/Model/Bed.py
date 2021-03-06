from NamedDescribedDataset import NamedDescribedDataset

from PyQt4.QtCore import *

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
        self.boundaryTypes = []
        self.outcropTypes = []
        self.facies = []
        self.lithologicalUnits = []
        self.stratigraphicUnits = []
        self.tectonicUnits = []
        self.geologicalMeasurements = []
        self.poi = None

        self.updateName()
    def hasNumber(self):
        return self.number is not None
    def hasLithology(self):
        return len(self.lithologies) > 0
    def hasColor(self):
        return len(self.colors) > 0
    def hasBeddingType(self):
        return len(self.beddingTypes) > 0
    def hasBoundaryType(self):
        return len(self.boundaryTypes) > 0
    def hasPoi(self):
        return self.poi is not None
    def hasBaseGrainSize(self):
        return self.baseGrainSize is not None
    def hasTopGrainSize(self):
        return self.topGrainSize is not None
    def hasCustomSymbol(self):
        return len(self.customSymbols) > 0
    def __str__(self):
        return self.name
    def hasOutcropType(self):
        return len(self.outcropTypes) > 0
    def heightInMillimetres(self):
        return self.height * self.lengthUnit.microMetre / 1000
    def updateName(self):
        self.name = unicode(QCoreApplication.translate('bed', "%1/%2/Bed #%3").arg(self.profile.project.name).arg(self.profile.name).arg(self.number, 5, 10, QChar('0')))
    def heightInPixel(self):
        return self.heightInMillimetres() / self.profile.scale
    def getFormattedHeight(self):
        return unicode(QString('%1 %2').arg(self.height).arg(unicode(self.lengthUnit.name)))
    def hasValidHeight(self):
        if self.height is None:
            return False
        if self.height <= 0:
            return False
        if self.lengthUnit is None:
            return False
        return True
