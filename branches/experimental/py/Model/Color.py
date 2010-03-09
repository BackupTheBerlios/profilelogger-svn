from NamedDescribedDatasetInProject import NamedDescribedDatasetInProject

class Color(NamedDescribedDatasetInProject):
    def __init__(self, project, id=None, name=None, description=None):
        super(Color, self).__init__(project, id, name, description)
        self.project.registerColor(self)
