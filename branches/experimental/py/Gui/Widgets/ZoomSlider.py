from Slider import *

class ZoomSlider(Slider):
    def __init__(self, parent):
        Slider.__init__(self, parent)
        self.setRange(0, 1000)
        self.setSingleStep(1)
        self.setValue(0)