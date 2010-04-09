from Gui.Dialogs.DatasetEditorDialog import *

from PyQt4.QtCore import *

class ProfileColumnEditorDialog(DatasetEditorDialog):
    def __init__(self, parent, data):
        DatasetEditorDialog.__init__(self, parent, data)
        self.addContentPanel(self.tr("Profile Column"))
        self.addIdDisplay()
        self.addNameEdit()
        self.addHeaderClassNameEdit()
        self.addBedPartClassNameEdit()
        self.addDescriptionEdit()
        self.addButtons()

        self.idW.setValue(self.data.id)
        self.nameW.setValue(unicode(self.data.name))
        self.headerClassNameW.setValue(unicode(self.data.headerClassName))
        self.bedPartClassNameW.setValue(unicode(self.data.bedPartClassName))
        self.descriptionW.setValue(unicode(self.data.description))

        self.nameW.nameChanged.connect(self.onNameChange)
        self.descriptionW.descriptionChanged.connect(self.onDescriptionChange)
    def onNameChange(self, txt):
        self.data.name = unicode(txt)
    def onDescriptionChange(self, txt):
        self.data.description = unicode(txt)
    def addHeaderClassNameEdit(self):
        self.headerClassNameL = self.createOneLineLabel(self.tr("Header Class Name"))
        self.headerClassNameW = NameEdit(self.contentW)
        self.addLabelWidgetPair(self.headerClassNameL, self.headerClassNameW)
        self.headerClassNameW.nameChanged.connect(self.onHeaderClassNameChange)
    def onHeaderClassNameChange(self, v):
        self.data.headerClassName = unicode(v)
    def addBedPartClassNameEdit(self):
        self.bedPartClassNameL = self.createOneLineLabel(self.tr("Bed Part Class Name"))
        self.bedPartClassNameW = NameEdit(self.contentW)
        self.addLabelWidgetPair(self.bedPartClassNameL, self.bedPartClassNameW)
        self.bedPartClassNameW.nameChanged.connect(self.onBedPartClassNameChange)
    def onBedPartClassNameChange(self, v):
        self.data.bedPartClassName = unicode(v)
