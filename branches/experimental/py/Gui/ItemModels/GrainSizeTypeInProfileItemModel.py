from DataInProfileManagementItemModel import DataInProfileManagementItemModel

from PyQt4.QtGui import *

from Model.GrainSizeTypeInProfile import GrainSizeTypeInProfile
from Gui.ItemModels.GrainSizeTypeInProfileItem import GrainSizeTypeInProfileItem
from Gui.Dialogs.GrainSizeTypeInProfileEditorDialog import GrainSizeTypeInProfileEditorDialog

class GrainSizeTypeInProfileItemModel(DataInProfileManagementItemModel):
    def __init__(self, parent):
        DataInProfileManagementItemModel.__init__(self, parent,
                                                  GrainSizeTypeInProfile,
                                                  GrainSizeTypeInProfileItem,
                                                  GrainSizeTypeInProfileEditorDialog,
                                                  GrainSizeTypeInProfile.id)
        self.headerStrings = [self.tr("Grain Size Types")]
