from StandardItem import StandardItem

class PenCapStyleItem(StandardItem):
    def __init__(self, penCapStyle):
        StandardItem.__init__(self, penCapStyle)
        self.showData()
