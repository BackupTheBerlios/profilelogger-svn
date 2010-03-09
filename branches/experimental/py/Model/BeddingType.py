from NamedDescribedDatasetInProject import NamedDescribedDatasetInProject

class BeddingType(NamedDescribedDatasetInProject):
    def __init__(self, project, id=None, name=None, description=None):
        super(BeddingType, self).__init__(project, id, name, description)
        self.project.registerBeddingType(self)
