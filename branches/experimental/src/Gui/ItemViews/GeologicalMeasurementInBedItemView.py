from DataInBedManagementItemView import DataInBedManagementItemView

from PyQt4.QtCore import *
from PyQt4.QtGui import *

class GeologicalMeasurementInBedItemView(DataInBedManagementItemView):
    def __init__(self, parent, model):
        DataInBedManagementItemView.__init__(self, parent, model)