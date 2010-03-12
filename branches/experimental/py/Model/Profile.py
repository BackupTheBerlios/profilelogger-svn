from NamedDescribedDatasetInProject import NamedDescribedDatasetInProject

class Profile(NamedDescribedDatasetInProject):
    def __init__(self, project, id=None, name=None, description=None):
        super(Profile, self).__init__(project, id, name, description)
        self.project.registerProfile(self)
        self.beds = []

    def registerBed(self, b):
        if self.beds.count(b) > 0:
            return
        self.beds.append(b)
