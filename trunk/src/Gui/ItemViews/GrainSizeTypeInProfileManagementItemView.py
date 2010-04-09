from DataInProfileManagementItemView import DataInProfileManagementItemView

from PyQt4.QtCore import *
from PyQt4.QtGui import *

class GrainSizeTypeInProfileManagementItemView(DataInProfileManagementItemView):
    def __init__(self, parent, model):
        DataInProfileManagementItemView.__init__(self, parent, model, askForConfirmationBeforeDeleting=False)
