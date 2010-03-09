from NamedDescribedDataset import NamedDescribedDataset

class Project(NamedDescribedDataset):
    def __init__(self, id=None, name=None, description=None):
        super(Project, self).__init__(id, name, description)
        self.lithologies = []
        self.colors = []
        self.beddingTypes = []
        self.sedimentStructures = []
        self.fossils = []
        self.customSymbols = []
        self.boundaryTypes = []
        self.pois = []
        self.profiles = []

    def registerProfile(self, p):
        if self.profiles.count(p) > 0:
            print 'Profile %s already registered in project %s' % (p, self.name)
            return
        self.profiles.append(p)
    def registerPointOfInterest(self, p):
        if self.pois.count(p) > 0:
            print 'POI %s already registered in project %s' % (p, self.name)
            return
        self.pois.append(p)

    def registerBoundaryType(self, t):
        if self.boundaryTypes.count(t) > 0:
            print 'Boundary Type %s already registered in project %s' % (t, self.name)
            return
        self.boundaryTypes.append(t)

    def registerCustomSymbol(self, s):
        if self.customSymbols.count(s) > 0:
            print 'Custom Symbol %s already registered in project %s' % (s, self.name)
            return
        self.customSymbols.append(s)

    def registerFossil(self, f):
        if self.fossils.count(f) > 0:
            print 'Fossil %s alread registered in project %s' % (f, self.name)
            return
        self.fossils.append(f)

    def registerSedimentStructure(self, s):
        if self.sedimentStructures.count(s) > 0:
            print 'Sediment Structure %s already registered in project %s' % (s, self.name)
            return
        self.sedimentStructures.append(s)

    def registerBeddingType(self, t):
        if self.beddingTypes.count(t) > 0:
            print 'Bedding Type %s already registered in project %s' % (t, self.name)
            return
        self.beddingTypes.append(t)

    def registerLithology(self, l):
        if self.lithologies.count(l) > 0:
            print 'Lithology %s already registered in project %s' % (l, self.name)
            return
        self.lithologies.append(l)
        
    def registerColor(self, c):
        if self.colors.count(c) > 0:
            print 'Color %s already registered in project %s' % (c, self.name)
            return
        self.colors.append(c)

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
        for p in self.pois:
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