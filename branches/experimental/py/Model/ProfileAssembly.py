from NamedDescribedDatasetInProject import NamedDescribedDatasetInProject

class ProfileAssembly(NamedDescribedDatasetInProject):
    def __init__(self, project, id=None, name=None, description=None):
        super(ProfileAssembly, self).__init__(project, id, name, description)
        self.project.registerProfileAssembly(self)
        self.beds = []

    def registerBed(self, b):
        if self.beds.count(b) > 0:
            return
        self.beds.append(b)
