from StandardItem import StandardItem

class BrushItem(StandardItem):
    def __init__(self, brush):
        StandardItem.__init__(self, brush)
        self.showData()
