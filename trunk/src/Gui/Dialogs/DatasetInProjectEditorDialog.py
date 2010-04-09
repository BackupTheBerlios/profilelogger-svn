from Gui.Dialogs.DatasetEditorDialog import *

from PyQt4.QtCore import *

from Gui.ItemViews.ProjectItemView import ProjectItemView

class DatasetInProjectEditorDialog(DatasetEditorDialog):
    def __init__(self, parent, data):
        DatasetEditorDialog.__init__(self, parent, data)
    def addProjectSelector(self):
        self.projectL = self.createMultiLineLabel(self.tr("&Project"))
        self.projectW = ProjectItemView(self.contentW, 
                                        QApplication.instance().projectModel)
        self.projectL.setBuddy(self.projectW)
        self.addLabelWidgetPair(self.projectL, self.projectW)
        self.projectW.currentDatasetChanged.connect(self.onProjectChange)
        QApplication.instance().projectModel.reload()
    def onProjectChange(self, project):
        self.data.project = project
