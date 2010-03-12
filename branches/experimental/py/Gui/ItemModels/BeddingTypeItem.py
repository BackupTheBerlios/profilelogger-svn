from StandardItem import StandardItem

class BeddingTypeItem(StandardItem):
    def __init__(self, beddingType):
        StandardItem.__init__(self, beddingType)
        self.showData()
