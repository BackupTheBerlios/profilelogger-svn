from Gui.Dialogs.DatasetInProfileEditorDialog import *

from PyQt4.QtCore import *
from PyQt4.QtGui import *

from Gui.ItemViews.GrainSizeTypeItemView import *

class GrainSizeTypeInProfileEditorDialog(DatasetInProfileEditorDialog):
    def __init__(self, parent, data):
        DatasetInProfileEditorDialog.__init__(self, parent, data)
        self.addContentPanel(self.tr("Grain Size Type In Profile"))
        self.addIdDisplay()
        self.addProfileSelector()
        self.addGrainSizeTypeSelector()
        self.addButtons()

        self.profileW.setSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Minimum)
        self.grainSizeTypeW.setSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Minimum)

        self.idW.setValue(self.data.id)
        self.profileW.selectDataset(data.profile)
        self.grainSizeTypeW.selectDataset(data.grainSizeType)

    def addGrainSizeTypeSelector(self):
        self.grainSizeTypeL = self.createMultiLineLabel(self.tr("Grain Size Type"))
        self.grainSizeTypeW = GrainSizeTypeItemView(self)
        self.addLabelWidgetPair(self.grainSizeTypeL, self.grainSizeTypeW)
        self.grainSizeTypeW.currentDatasetChanged.connect(self.onGrainSizeTypeChange)
        self.grainSizeTypeW.reload()
    def onGrainSizeTypeChange(self, s):
        self.data.grainSizeType = s
