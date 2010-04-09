from NamedDescribedDataset import NamedDescribedDataset

class NamedDescribedDatasetInProject(NamedDescribedDataset):
    def __init__(self, project, id=None, name=None, description=None):
        super(NamedDescribedDatasetInProject, self).__init__(id, name, description)
        self.project = project
    def hasProject(self):
        return self.project is not None
