from StandardItem import StandardItem

class ColumnInProfileItem(StandardItem):
    def __init__(self, ColumnInProfile):
        StandardItem.__init__(self, ColumnInProfile)
        self.showData()
    def showData(self):
        self.setText(unicode(self.data.profileColumn.name))
        self.setToolTip(unicode(self.data.profileColumn.makeToolTip()))
