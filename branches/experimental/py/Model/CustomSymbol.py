from NamedDescribedDatasetInProject import NamedDescribedDatasetInProject

class CustomSymbol(NamedDescribedDatasetInProject):
    def __init__(self, project, id=None, name=None, description=None):
        super(CustomSymbol, self).__init__(project, id, name, description)
        self.project.registerCustomSymbol(self)
