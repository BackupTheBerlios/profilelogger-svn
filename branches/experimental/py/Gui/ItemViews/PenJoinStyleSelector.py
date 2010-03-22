from DataSelectionComboBox import DataSelectionComboBox

from PyQt4.QtCore import *
from PyQt4.QtGui import *

class PenJoinStyleSelector(DataSelectionComboBox):
    def __init__(self, parent, model):
        DataSelectionComboBox.__init__(self, parent, model)
