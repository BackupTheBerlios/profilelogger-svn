from NamedDescribedDatasetInProject import NamedDescribedDatasetInProject

class Fossil(NamedDescribedDatasetInProject):
    def __init__(self, project, id=None, name=None, description=None):
        super(Fossil, self).__init__(project, id, name, description)
        self.project.registerFossil(self)
