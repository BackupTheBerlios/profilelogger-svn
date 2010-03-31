from StandardItem import StandardItem

class PenJoinStyleItem(StandardItem):
    def __init__(self, penJoinStyle):
        StandardItem.__init__(self, penJoinStyle)
        self.showData()
