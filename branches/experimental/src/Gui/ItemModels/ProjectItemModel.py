from DataManagementItemModel import DataManagementItemModel

from PyQt4.QtGui import *

from Model.Project import Project
from Gui.ItemModels.ProjectItem import ProjectItem
from Gui.Dialogs.ProjectEditorDialog import ProjectEditorDialog

class ProjectItemModel(DataManagementItemModel):
    def __init__(self, parent):
        DataManagementItemModel.__init__(self, parent,
                                         Project,
                                         ProjectItem,
                                         ProjectEditorDialog,
                                         Project.name)
        self.headerStrings = [self.tr("Projects")]
