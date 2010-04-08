from NamedDescribedDatasetInProject import NamedDescribedDatasetInProject

from Bed import Bed

class Profile(NamedDescribedDatasetInProject):
    def __init__(self, project, 
                 id=None, name=None, description=None, 
                 startHeightValue=0, startHeightLengthUnit=None,
                 scale=1,
                 bigMarksDistanceValue=None, bigMarksDistanceLengthUnit=None,
                 smallMarksDistanceValue=None, smallMarksDistanceLengthUnit=None,
                 colsInLegend=10):
        super(Profile, self).__init__(project, id, name, description)
        self.startHeightValue = startHeightValue
        self.startHeightLengthUnit = startHeightLengthUnit
        self.grainSizeTypes = []
        self.beds = []
        self.scale = scale
        self.bigMarksDistanceValue = bigMarksDistanceValue
        self.bigMarksDistanceLengthUnit = bigMarksDistanceLengthUnit
        self.smallMarksDistanceValue = smallMarksDistanceValue
        self.smallMarksDistanceLengthUnit = smallMarksDistanceLengthUnit
        self.colsInLegend = self.colsInLegend
    def createBedOnTop(self):
        newBedNumber = self.getMaxBedNumber()
        if newBedNumber is None:
            newBedNumber = 1
        else:
            newBedNumber += 1
        return Bed(self, None,
                   0, None,
                   newBedNumber)
    def createBedAtBottom(self):
        newBedNumber = self.getMinBedNumber()
        if newBedNumber is None:
            newBedNumber = 1
        else:
            newBedNumber -= 1
        return Bed(self, None,
                   0, None,
                   newBedNumber)
    def getMinBedNumber(self):
        ret = None
        for b in self.beds:
            if ret is None:
                ret = b.number 
            else:
                if b.number < ret:
                    ret = b.number
        return ret
    def getMaxBedNumber(self):
        ret = None
        for b in self.beds:
            if ret is None:
                ret = b.number 
            else:
                if b.number > ret:
                    ret = b.number
        return ret
    def heightInMillimetres(self):
        r = 0
        for b in self.beds:
            r += b.height * b.lengthUnit.microMetre / 1000
        return r
    def displayWidth(self):
        tot = 0
        for c in self.columns:
            tot += c.width
        return tot
    def heightInPixel(self):
        ret = 0
        for b in self.beds:
            ret += b.heightInPixel()
        return ret
