from Gui.Dialogs.DatasetInProjectEditorDialog import *

from PyQt4.QtCore import *

from Gui.ItemViews.ProjectItemView import ProjectItemView
from Gui.ItemViews.DrawingItemView import DrawingItemView

class DatasetWithDrawingInProjectEditorDialog(DatasetInProjectEditorDialog):
    def __init__(self, parent, data):
        DatasetInProjectEditorDialog.__init__(self, parent, data)
    def addDrawingSelector(self):
        self.drawingL = self.createMultiLineLabel(self.tr("&Representation"))
        self.drawingW = DrawingItemView(self.contentW, 
                                        QApplication.instance().drawingModel)
        self.drawingL.setBuddy(self.drawingW)
        self.addLabelWidgetPair(self.drawingL, self.drawingW)
        self.drawingW.currentDatasetChanged.connect(self.onDrawingChange)
    def onDrawingChange(self, itm):
        self.data.drawing = itm
