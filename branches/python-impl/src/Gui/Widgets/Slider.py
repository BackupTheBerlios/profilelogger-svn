from PyQt4.QtGui import *
from PyQt4.QtCore import *

class Slider(QSlider):
    def __init__(self, parent):
        QSlider.__init__(self, parent)
