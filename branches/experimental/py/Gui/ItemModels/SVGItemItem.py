from StandardItem import StandardItem

class SVGItemItem(StandardItem):
    def __init__(self, svgItem):
        StandardItem.__init__(self, svgItem)
        self.showData()
