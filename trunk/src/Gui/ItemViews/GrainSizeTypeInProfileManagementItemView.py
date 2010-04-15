from DataInProfileManagementItemView import DataInProfileManagementItemView

from PyQt4.QtCore import *
from PyQt4.QtGui import *

from Gui.ItemModels.GrainSizeTypeInProfileItemModel import *

class GrainSizeTypeInProfileManagementItemView(DataInProfileManagementItemView):
    def __init__(self, parent):
        DataInProfileManagementItemView.__init__(self, parent, 
                                                 askForConfirmationBeforeDeleting=False)
        self.configureModel(GrainSizeTypeInProfileItemModel(self))
