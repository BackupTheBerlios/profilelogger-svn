from StandardItem import StandardItem

class FaciesItem(StandardItem):
    def __init__(self, facies):
        StandardItem.__init__(self, facies)
        self.showData()
