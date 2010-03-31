from StandardItem import StandardItem

class DrawingItem(StandardItem):
    def __init__(self, drawing):
        StandardItem.__init__(self, drawing)
        self.showData()
