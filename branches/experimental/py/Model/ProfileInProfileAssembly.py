from NamedDescribedDataset import NamedDescribedDataset

class ProfileInProfileAssembly(NamedDescribedDataset):
    def __init__(self, profileAssembly, id=None, name=None, description=None):
        super(ProfileInProfileAssembly, self).__init__(id, name, description)
        self.profileAssembly = profileAssembly
        self.profileAssembly.registerProfileInProfileAssembly(self)
