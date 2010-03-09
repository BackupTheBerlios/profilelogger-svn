from NamedDescribedDatasetInProject import NamedDescribedDatasetInProject

class GrainSize(NamedDescribedDatasetInProject):
    def __init__(self, project, id=None, name=None, description=None):
        super(GrainSize, self).__init__(project, id, name, description)
        self.project.registerGrainSize(self)
