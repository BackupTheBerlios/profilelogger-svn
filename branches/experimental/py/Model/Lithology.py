from NamedDescribedDatasetWithSVGItemInProject import NamedDescribedDatasetWithSVGItemInProject

class Lithology(NamedDescribedDatasetWithSVGItemInProject):
    def __init__(self, project, id=None, name=None, svgItem=None, description=None, defaultGrainSize=None):
        super(Lithology, self).__init__(project, id, name, svgItem, description)
        self.project.registerLithology(self)
        self.defaultGrainSize = None
    def hasDefaultGrainSize(self):
        return self.defaultGrainSize is not None
    def __str__(self):
        return u'<Lithology: Name: %s>' % (self.name)
