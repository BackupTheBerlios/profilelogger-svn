from NamedDescribedDatasetInProject import NamedDescribedDatasetInProject

class Profile(NamedDescribedDatasetInProject):
    def __init__(self, project, 
                 id=None, name=None, description=None, 
                 startHeightValue=0, startHeightLengthUnit=None,
                 scale=1,
                 bigMarksDistanceValue=None, bigMarksDistanceLengthUnit=None,
                 smallMarksDistanceValue=None, smallMarksDistanceLengthUnit=None):
        super(Profile, self).__init__(project, id, name, description)
        self.project.registerProfile(self)
        self.startHeightValue = startHeightValue
        self.startHeightLengthUnit = startHeightLengthUnit
        self.grainSizeTypes = []
        self.beds = []
        self.scale = scale
        self.bigMarksDistanceValue = bigMarksDistanceValue
        self.bigMarksDistanceLengthUnit = bigMarksDistanceLengthUnit
        self.smallMarksDistanceValue = smallMarksDistanceValue
        self.smallMarksDistanceLengthUnit = smallMarksDistanceLengthUnit

    def registerBed(self, b):
        if self.beds.count(b) > 0:
            return
        self.beds.append(b)
    def heightInMillimetres(self):
        r = 0
        for b in self.beds:
            r += b.height * b.lengthUnit.microMetre / 1000
        return r