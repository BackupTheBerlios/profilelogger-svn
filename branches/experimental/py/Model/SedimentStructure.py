from NamedDescribedDatasetInProject import NamedDescribedDatasetInProject

class SedimentStructure(NamedDescribedDatasetInProject):
    def __init__(self, project, id=None, name=None, description=None):
        super(SedimentStructure, self).__init__(project, id, name, description)
        self.project.registerSedimentStructure(self)
