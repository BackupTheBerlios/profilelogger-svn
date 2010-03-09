from NamedDescribedDatasetInProject import NamedDescribedDatasetInProject

class Lithology(NamedDescribedDatasetInProject):
    def __init__(self, project, id=None, name=None, description=None):
        super(Lithology, self).__init__(project, id, name, description)
        self.project.registerLithology(self)
    def __str__(self):
        return u'<Lithology: ID: %i, Name: %s>' % (self.id, self.name)
