from NamedDescribedDatasetWithDrawingInProject import NamedDescribedDatasetWithDrawingInProject

class Lithology(NamedDescribedDatasetWithDrawingInProject):
    def __init__(self, project, id=None, name=None, drawing=None, description=None, defaultGrainSize=None):
        super(Lithology, self).__init__(project, id, name, drawing, description)
        self.project.registerLithology(self)
        self.defaultGrainSize = defaultGrainSize
    def hasDefaultGrainSize(self):
        return self.defaultGrainSize is not None
    def __str__(self):
        return u'<Lithology: Name: %s>' % (self.name)
