from NamedDescribedDatasetInProject import NamedDescribedDatasetInProject

class PointOfInterest(NamedDescribedDatasetInProject):
    def __init__(self, project, id=None, name=None, description=None):
        super(PointOfInterest, self).__init__(project, id, name, description)
        self.project.registerPointOfInterest(self)
