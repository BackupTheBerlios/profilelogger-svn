from DataManagementItemView import DataManagementItemView

from PyQt4.QtCore import *
from PyQt4.QtGui import *

class LithologicalUnitItemView(DataManagementItemView):
    def __init__(self, parent, model):
        DataManagementItemView.__init__(self, parent, model)
