from Gui.Dialogs.DatasetWithSvgItemInProjectEditorDialog import *

from PyQt4.QtCore import *

from Gui.ItemViews.GrainSizeItemView import GrainSizeItemView

class LithologyEditorDialog(DatasetWithSvgItemInProjectEditorDialog):
    def __init__(self, parent, data):
        DatasetWithSvgItemInProjectEditorDialog.__init__(self, parent, data)
        self.addContentPanel(self.tr("Lithology"))
        self.addIdDisplay()
        self.addProjectSelector()
        self.addSvgItemSelector()
        self.addGrainSizeSelector()
        self.addNameEdit()
        self.addDescriptionEdit()
        self.addButtons()

        self.idW.setValue(self.data.id)
        self.projectW.selectDataset(data.project)
        self.grainSizeW.selectDataset(data.defaultGrainSize)
        self.svgItemW.selectDataset(data.svgItem)
        self.nameW.setValue(unicode(self.data.name))
        self.descriptionW.setValue(unicode(self.data.description))

        self.nameW.nameChanged.connect(self.onNameChange)
        self.descriptionW.descriptionChanged.connect(self.onDescriptionChange)
    def onNameChange(self, txt):
        self.data.name = unicode(txt)
    def onDescriptionChange(self, txt):
        self.data.description = unicode(txt)
    def addGrainSizeSelector(self):
        self.grainSizeL = self.createMultiLineLabel(self.tr("&Default Grain Size"))
        self.grainSizeW = GrainSizeItemView(self)
        self.grainSizeL.setBuddy(self.grainSizeW)
        self.addLabelWidgetPair(self.grainSizeL, self.grainSizeW)
        self.grainSizeW.currentDatasetChanged.connect(self.onGrainSizeChange)
        self.grainSizeW.reload()
    def onGrainSizeChange(self, grainSize):
        self.data.defaultGrainSize = grainSize
