from StandardItem import StandardItem

class ProfileItem(StandardItem):
    def __init__(self, profile):
        StandardItem.__init__(self, profile)
        self.showData()
