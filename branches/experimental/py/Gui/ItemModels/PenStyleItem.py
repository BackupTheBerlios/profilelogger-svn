from StandardItem import StandardItem

class PenStyleItem(StandardItem):
    def __init__(self, penStyle):
        StandardItem.__init__(self, penStyle)
        self.showData()
