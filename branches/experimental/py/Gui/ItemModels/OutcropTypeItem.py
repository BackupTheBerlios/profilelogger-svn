from StandardItem import StandardItem

class OutcropTypeItem(StandardItem):
    def __init__(self, outcropType):
        StandardItem.__init__(self, outcropType)
        self.showData()
