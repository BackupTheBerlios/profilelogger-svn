from Gui.Dialogs.DatasetEditorDialog import *

from PyQt4.QtCore import *

from Gui.ItemViews.GrainSizeTypeItemView import GrainSizeTypeItemView

class GrainSizeEditorDialog(DatasetEditorDialog):
    def __init__(self, parent, data):
        DatasetEditorDialog.__init__(self, parent, data)
        self.addContentPanel(self.tr("Grain Size"))
        self.addIdDisplay()
        self.addNameEdit()
        
        self.typeL = self.createOneLineLabel(self.tr("Grain Size Type"))
        self.typeW = GrainSizeTypeItemView(self.contentW,
                                           QApplication.instance().grainSizeTypeModel)
        self.addLabelWidgetPair(self.typeL, self.typeW)

        self.addDescriptionEdit()
        self.addButtons()

        self.idW.setValue(self.data.id)
        self.nameW.setValue(unicode(self.data.name))
        self.descriptionW.setValue(unicode(self.data.description))
        self.typeW.selectDataset(self.data.grainSizeType)

        self.nameW.nameChanged.connect(self.onNameChange)
        self.descriptionW.descriptionChanged.connect(self.onDescriptionChange)
        self.typeW.currentDatasetChanged.connect(self.onGrainSizeTypeChange)
    def onNameChange(self, txt):
        self.data.name = unicode(txt)
    def onDescriptionChange(self, txt):
        self.data.description = unicode(txt)
    def onGrainSizeTypeChange(self, t):
        print "class: ",t.__class__.__name__
        self.data.grainSizeType = t
