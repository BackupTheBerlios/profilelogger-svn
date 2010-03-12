from StandardItem import StandardItem

class FossilItem(StandardItem):
    def __init__(self, fossil):
        StandardItem.__init__(self, fossil)
        self.showData()
