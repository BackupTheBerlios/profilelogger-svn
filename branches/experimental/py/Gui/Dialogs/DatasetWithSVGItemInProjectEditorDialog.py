from Gui.Dialogs.DatasetInProjectEditorDialog import *

from PyQt4.QtCore import *

from Gui.ItemViews.ProjectItemView import ProjectItemView
from Gui.ItemViews.SVGItemView import SVGItemView

class DatasetWithSVGItemInProjectEditorDialog(DatasetInProjectEditorDialog):
    def __init__(self, parent, data):
        DatasetInProjectEditorDialog.__init__(self, parent, data)
    def addSVGItemSelector(self):
        self.svgItemL = self.createMultiLineLabel(self.tr("&Graphic Representation"))
        self.svgItemW = SVGItemView(self.contentW, 
                                    QApplication.instance().svgItemModel)
        self.svgItemL.setBuddy(self.svgItemW)
        self.addLabelWidgetPair(self.svgItemL, self.svgItemW)
        self.svgItemW.currentDatasetChanged.connect(self.onSvgItemChange)
#        QApplication.instance().svgItemModel.reload()
    def onSvgItemChange(self, itm):
        self.data.svgItem = itm
