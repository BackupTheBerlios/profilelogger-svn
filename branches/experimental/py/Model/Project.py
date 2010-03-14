from NamedDescribedDataset import NamedDescribedDataset

class Project(NamedDescribedDataset):
    def __init__(self, id=None, name=None, description=None):
        super(Project, self).__init__(id, name, description)
        self.lithologies = []
        self.colors = []
        self.outcropTypes = []
        self.beddingTypes = []
        self.sedimentStructures = []
        self.fossils = []
        self.customSymbols = []
        self.boundaryTypes = []
        self.pointsOfInterest = []
        self.profiles = []
        self.facies = []
        self.lithologicalUnits = []
        self.tectonicUnits = []
        self.stratigraphicUnits = []
        self.geologicalMeasurementTypes = []
        self.profileAssemblies = []
    def registerProfile(self, p):
        if self.profiles.count(p) > 0:
            return
        self.profiles.append(p)
    def registerPointOfInterest(self, p):
        if self.pointsOfInterest.count(p) > 0:
            return
        self.pointsOfInterest.append(p)

    def registerBoundaryType(self, t):
        if self.boundaryTypes.count(t) > 0:
            return
        self.boundaryTypes.append(t)

    def registerCustomSymbol(self, s):
        if self.customSymbols.count(s) > 0:
            return
        self.customSymbols.append(s)

    def registerFossil(self, f):
        if self.fossils.count(f) > 0:
            return
        self.fossils.append(f)

    def registerSedimentStructure(self, s):
        if self.sedimentStructures.count(s) > 0:
            return
        self.sedimentStructures.append(s)

    def registerBeddingType(self, t):
        if self.beddingTypes.count(t) > 0:
            return
        self.beddingTypes.append(t)

    def registerLithology(self, l):
        if self.lithologies.count(l) > 0:
            return
        self.lithologies.append(l)
        
    def registerColor(self, c):
        if self.colors.count(c) > 0:
            return
        self.colors.append(c)
    def registerOutcropType(self, c):
        if self.outcropTypes.count(c) > 0:
            return
        self.outcropTypes.append(c)
    def registerFacies(self, c):
        if self.facies.count(c) > 0:
            return
        self.facies.append(c)

    def debug(self):
        print 'Project: %s' % self.name
        print '\tLithologies:'
        for l in self.lithologies:
            print '\t\t%s' % l
        print '\tColors:'
        for c in self.colors:
            print '\t\t%s' % c
        print '\tBedding Types:'
        for t in self.beddingTypes:
            print '\t\t%s' % t
        print '\tSediment Structures:'
        for s in self.sedimentStructures:
            print '\t\t%s' % s
        print '\tFossils:'
        for f in self.fossils:
            print '\t\t%s' % f
        print '\tCustom Symbols:'
        for s in self.customSymbols:
            print '\t\t%s' % s
        print '\tBoundary Types:'
        for t in self.boundaryTypes:
            print '\t\t%s' % s
        print '\tPoints of Interest:'
        for p in self.pointsOfInterest:
            print '\t\t%s' % p
        print '\tProfiles:'
        for p in self.profiles:
            print '\t\t%s' % p
            for b in p.beds:
                print '\t\t\t%s' % b
                for lib in b.lithologies:
                    print '\t\t\t\t\t%s' % lib
                for c in b.colors:
                    print '\t\t\t\t\t%s' % c
                for t in b.beddingTypes:
                    print '\t\t\t\t\t%s' % t
                for s in b.customSymbols:
                    print '\t\t\t\t\t%s' % s
                for s in b.sedimentStructures:
                    print '\t\t\t\t\t%s' % s
                for f in b.fossils:
                    print '\t\t\t\t\t%s' % f
    def registerLithologicalUnit(self, c):
        if self.lithologicalUnits.count(c) > 0:
            return
        self.lithologicalUnits.append(c)
    def registerTectonicUnit(self, c):
        if self.tectonicUnits.count(c) > 0:
            return
        self.tectonicUnits.append(c)
    def registerStratigraphicUnit(self, c):
        if self.stratigraphicUnits.count(c) > 0:
            return
        self.stratigraphicUnits.append(c)
    def registerProfileAssembly(self, p):
        if self.profileAssemblies.count(p) > 0:
            return
        self.profileAssemblies.append(p)
