from NamedDescribedDatasetInProject import NamedDescribedDatasetInProject

class BoundaryType(NamedDescribedDatasetInProject):
    def __init__(self, project, id=None, name=None, description=None):
        super(BoundaryType, self).__init__(project, id, name, description)
        self.project.registerBoundaryType(self)
