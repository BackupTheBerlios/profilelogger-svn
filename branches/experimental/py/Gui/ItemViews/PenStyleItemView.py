from DataSelectionComboBox import DataSelectionComboBox

from PyQt4.QtCore import *
from PyQt4.QtGui import *

class PenStyleItemView(DataSelectionComboBox):
    def __init__(self, parent, model):
        DataManagementItemView.__init__(self, parent, model)
