from Gui.Dialogs.DatasetEditorDialog import *

from PyQt4.QtCore import *

class ProjectEditorDialog(DatasetEditorDialog):
    def __init__(self, parent, data):
        DatasetEditorDialog.__init__(self, parent, data)
        self.addContentPanel(self.tr("Project"))
        self.addIdDisplay()
        self.addNameEdit()
        self.addDescriptionEdit()
        self.addButtons()

        self.idW.setValue(self.data.id)
        self.nameW.setValue(str(self.data.name))
        self.descriptionW.setValue(str(self.data.description))

        self.nameW.nameChanged.connect(self.onNameChange)
        self.descriptionW.descriptionChanged.connect(self.onDescriptionChange)
    def onNameChange(self, txt):
        self.data.name = str(txt)
    def onDescriptionChange(self, txt):
        self.data.description = str(txt)
