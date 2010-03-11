from Gui.Dialogs.DatasetEditorDialog import *

from PyQt4.QtCore import *

class LengthUnitEditorDialog(DatasetEditorDialog):
    def __init__(self, parent, data):
        DatasetEditorDialog.__init__(self, parent, data)
        self.addContentPanel(self.tr("Length Unit"))
        self.addIdDisplay()
        self.addNameEdit()
        self.addIntEdit(self.tr("&Micrometres"))
        self.addDescriptionEdit()
        self.addButtons()

        self.idW.setValue(self.data.id)
        self.nameW.setValue(unicode(self.data.name))
        self.intW.setValue(self.data.microMetre)
        self.descriptionW.setValue(unicode(self.data.description))

        self.nameW.nameChanged.connect(self.onNameChange)
        self.intW.valueChanged.connect(self.onMillimetreChange)
        self.descriptionW.descriptionChanged.connect(self.onDescriptionChange)
    def onNameChange(self, txt):
        self.data.name = unicode(txt)
    def onMillimetreChange(self, mm):
        self.data.microMetre = mm
    def onDescriptionChange(self, txt):
        self.data.description = unicode(txt)
