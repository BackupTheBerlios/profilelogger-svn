from Gui.Dialogs.DatasetInProjectEditorDialog import *

from PyQt4.QtCore import *

from Gui.ItemViews.ProjectItemView import ProjectItemView
from Gui.ItemViews.SVGItemView import SVGItemView

class DatasetWithSvgItemInProjectEditorDialog(DatasetInProjectEditorDialog):
    def __init__(self, parent, data):
        DatasetInProjectEditorDialog.__init__(self, parent, data)
    def addSvgItemSelector(self):
        self.svgItemL = self.createMultiLineLabel(self.tr("&Representation"))
        self.svgItemW = SVGItemView(self.contentW)
        self.svgItemL.setBuddy(self.svgItemW)
        self.addLabelWidgetPair(self.svgItemL, self.svgItemW)
        self.svgItemW.currentDatasetChanged.connect(self.onSvgItemChange)
        self.svgItemW.reload()
    def onSvgItemChange(self, itm):
        self.data.svgItem = itm
