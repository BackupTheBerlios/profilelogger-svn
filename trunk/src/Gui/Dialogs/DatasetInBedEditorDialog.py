from Gui.Dialogs.DatasetEditorDialog import *

from PyQt4.QtCore import *

from Gui.ItemViews.BedItemView import BedItemView
from Gui.Widgets.PercentRangeEditorWidget import PercentRangeEditorWidget

class DatasetInBedEditorDialog(DatasetEditorDialog):
    def __init__(self, parent, data):
        DatasetEditorDialog.__init__(self, parent, data)
    def addBedSelector(self):
        self.bedL = self.createMultiLineLabel(self.tr("&Bed"))
        self.bedW = BedItemView(self.contentW, 
                                        QApplication.instance().bedModel)
        self.bedL.setBuddy(self.bedW)
        self.addLabelWidgetPair(self.bedL, self.bedW)
        self.bedW.currentDatasetChanged.connect(self.onBedChange)
        QApplication.instance().bedModel.reload()
    def onBedChange(self, bed):
        self.data.bed = bed
    def addPercentEditor(self):
        self.percentL = self.createOneLineLabel(self.tr("&Percent From Bottom"))
        self.percentW = PercentRangeEditorWidget(self.contentW)
        self.percentL.setBuddy(self.percentW)
        self.addLabelWidgetPair(self.percentL, self.percentW)
        self.percentW.beginValueChanged.connect(self.onBeginChange)
        self.percentW.endValueChanged.connect(self.onEndChange)
    def onBeginChange(self, v):
        self.data.begin = v
    def onEndChange(self, v):
        self.data.end
