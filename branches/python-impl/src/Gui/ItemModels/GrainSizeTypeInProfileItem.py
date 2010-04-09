from StandardItem import StandardItem

class GrainSizeTypeInProfileItem(StandardItem):
    def __init__(self, grainSizeTypeInProfile):
        StandardItem.__init__(self, grainSizeTypeInProfile)
        self.showData()
    def showData(self):
        self.setText(unicode(self.data.grainSizeType.name))
        self.setToolTip(unicode(self.data.grainSizeType.makeToolTip()))
