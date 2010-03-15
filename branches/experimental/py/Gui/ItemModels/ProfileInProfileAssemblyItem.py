from StandardItem import StandardItem

class ProfileInProfileAssemblyItem(StandardItem):
    def __init__(self, profileInProfileAssembly):
        StandardItem.__init__(self, profileInProfileAssembly)
        self.showData()
