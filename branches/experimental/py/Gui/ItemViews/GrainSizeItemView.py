from DataManagementItemView import DataManagementItemView

from PyQt4.QtCore import *
from PyQt4.QtGui import *

class GrainSizeItemView(DataManagementItemView):
    def __init__(self, parent, model):
        DataManagementItemView.__init__(self, parent, model)
