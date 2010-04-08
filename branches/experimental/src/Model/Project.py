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
