from StandardItem import StandardItem

class ProfileAssemblyItem(StandardItem):
    def __init__(self, profileAssembly):
        StandardItem.__init__(self, profileAssembly)
        self.showData()
