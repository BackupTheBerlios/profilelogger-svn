from StandardItem import StandardItem

class BrushStyleItem(StandardItem):
    def __init__(self, brushStyle):
        StandardItem.__init__(self, brushStyle)
        self.showData()
