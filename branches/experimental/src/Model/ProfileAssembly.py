from NamedDescribedDatasetInProject import NamedDescribedDatasetInProject

class ProfileAssembly(NamedDescribedDatasetInProject):
    def __init__(self, project, id=None, name=None, description=None):
        super(ProfileAssembly, self).__init__(project, id, name, description)
        self.beds = []
        self.profilesInProfileAssembly = []
