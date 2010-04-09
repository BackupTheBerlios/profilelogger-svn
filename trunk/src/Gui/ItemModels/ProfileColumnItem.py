from StandardItem import StandardItem

class ProfileColumnItem(StandardItem):
    def __init__(self, profileColumn):
        StandardItem.__init__(self, profileColumn)
        self.showData()
