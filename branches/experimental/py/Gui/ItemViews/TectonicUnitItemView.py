from DataInProjectManagementItemView import DataInProjectManagementItemView

from PyQt4.QtCore import *
from PyQt4.QtGui import *

class TectonicUnitItemView(DataInProjectManagementItemView):
    def __init__(self, parent, model):
        DataInProjectManagementItemView.__init__(self, parent, model)
