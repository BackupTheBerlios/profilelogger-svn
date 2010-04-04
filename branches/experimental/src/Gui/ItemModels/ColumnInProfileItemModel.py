from DataInProfileManagementItemModel import DataInProfileManagementItemModel

from PyQt4.QtGui import *

from Model.ColumnInProfile import ColumnInProfile
from Gui.ItemModels.ColumnInProfileItem import ColumnInProfileItem
from Gui.Dialogs.ColumnInProfileEditorDialog import ColumnInProfileEditorDialog

class ColumnInProfileItemModel(DataInProfileManagementItemModel):
    def __init__(self, parent):
        DataInProfileManagementItemModel.__init__(self, parent,
                                                  ColumnInProfile,
                                                  ColumnInProfileItem,
                                                  ColumnInProfileEditorDialog,
                                                  ColumnInProfile.position)
        self.headerStrings = [self.tr("Columns In Profile")]
