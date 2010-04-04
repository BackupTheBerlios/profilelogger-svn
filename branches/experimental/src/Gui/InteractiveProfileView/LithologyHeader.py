from LegendHeader import *

class LithologyHeader(LegendHeader):
    def __init__(self, parent, font=None, pos=None):
        LegendHeader.__init__(self, parent, font, pos)
        self.setText(unicode(QCoreApplication.instance().translate('lithology legend header', "Lithologies")))
