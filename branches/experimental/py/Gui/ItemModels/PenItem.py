from StandardItem import StandardItem

class PenItem(StandardItem):
    def __init__(self, pen):
        StandardItem.__init__(self, pen)
        self.showData()
