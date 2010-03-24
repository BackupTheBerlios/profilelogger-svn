from Gui.Dialogs.DatasetWithDrawingInProjectEditorDialog import *

from PyQt4.QtCore import *

from Gui.ItemViews.GrainSizeItemView import GrainSizeItemView

class CustomSymbolEditorDialog(DatasetWithDrawingInProjectEditorDialog):
    def __init__(self, parent, data):
        DatasetWithDrawingInProjectEditorDialog.__init__(self, parent, data)
        self.addContentPanel(self.tr("Custom Symbol"))
        self.addIdDisplay()
        self.addProjectSelector()
        self.addDrawingSelector()
        self.addNameEdit()
        self.addDescriptionEdit()
        self.addButtons()

        self.idW.setValue(self.data.id)
        self.projectW.selectDataset(data.project)
        self.drawingW.selectDataset(data.drawing)
        self.nameW.setValue(unicode(self.data.name))
        self.descriptionW.setValue(unicode(self.data.description))

        self.nameW.nameChanged.connect(self.onNameChange)
        self.descriptionW.descriptionChanged.connect(self.onDescriptionChange)
    def onNameChange(self, txt):
        self.data.name = unicode(txt)
    def onDescriptionChange(self, txt):
        self.data.description = unicode(txt)
