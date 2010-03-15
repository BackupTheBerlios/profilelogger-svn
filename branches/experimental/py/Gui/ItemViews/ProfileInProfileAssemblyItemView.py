from DataInProfileAssemblyManagementItemView import DataInProfileAssemblyManagementItemView

from PyQt4.QtCore import *
from PyQt4.QtGui import *

class ProfileInProfileAssemblyItemView(DataInProfileAssemblyManagementItemView):
    def __init__(self, parent, model):
        DataInProfileAssemblyManagementItemView.__init__(self, parent, model)
