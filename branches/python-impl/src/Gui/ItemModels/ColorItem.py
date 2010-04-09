from StandardItem import StandardItem

class ColorItem(StandardItem):
    def __init__(self, color):
        StandardItem.__init__(self, color)
        self.showData()
