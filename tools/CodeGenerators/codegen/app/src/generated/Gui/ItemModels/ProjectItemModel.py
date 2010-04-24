from ManagementItemModel import ManagementItemModel

from PyQt4.QtGui import *

from Logic.Model.Project import Project
from Gui.Dialogs.ProjectEditorDialog import ProjectEditorDialog
from ManagmentItemModel import *

class ProjectItem(StandardItem):
    def __init__(self, entity):
        StandardItem.__init__(self, entity)
        self.showData()

class ProjectItemModel(ManagementItemModel):
    def __init__(self, parent):
        ManagementItemModel.__init__(self, parent,
                                     Project,
                                     ProjectItem,
                                     ProjectEditorDialog,
                                     ProjectFinder)
        self.headerStrings = [self.tr('Projects')]
