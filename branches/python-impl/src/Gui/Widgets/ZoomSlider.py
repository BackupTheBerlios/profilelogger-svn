from Slider import *

class ZoomSlider(Slider):
    def __init__(self, parent):
        Slider.__init__(self, parent)
        self.setRange(-80, 5000)
        self.setSingleStep(10)
        self.setValue(0)
        
