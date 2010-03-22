from Gui.Dialogs.DatasetEditorDialog import *

from PyQt4.QtCore import *

from Gui.ItemViews.BrushStyleSelector import *
from Gui.Widgets.ColorSelectionWidget import *

class BrushEditorDialog(DatasetEditorDialog):
    def __init__(self, parent, data):
        DatasetEditorDialog.__init__(self, parent, data)
        self.addContentPanel(self.tr("Brush"))
        self.addIdDisplay()
        self.addNameEdit()
        self.addColorSelector()
        self.addBrushStyleSelector()
        self.addDescriptionEdit()
        self.addButtons()

        self.idW.setValue(self.data.id)
        self.nameW.setValue(unicode(self.data.name))
        self.colorW.setColor(self.data.getColor())
        self.brushStyleW.setValue(self.data.brushStyle)
        self.descriptionW.setValue(unicode(self.data.description))

        self.nameW.nameChanged.connect(self.onNameChange)
        self.descriptionW.descriptionChanged.connect(self.onDescriptionChange)
    def onNameChange(self, txt):
        self.data.name = unicode(txt)
    def onDescriptionChange(self, txt):
        self.data.description = unicode(txt)
    def addColorSelector(self):
        self.colorL = self.createOneLineLabel(self.tr("Brush Color"))
        self.colorW = ColorSelectionWidget(self.contentW)
        self.colorL.setBuddy(self.colorW)
        self.addLabelWidgetPair(self.colorL, self.colorW)
        self.colorW.colorChanged.connect(self.onBrushColorChange)
    def onBrushColorChange(self, c):
        if c is None:
            self.data.rgbRed = 0
            self.data.rgbGreen = 0
            self.data.rgbBlue = 0
            self.data.rgbAlpha = 255
            return
        self.data.rgbRed = c.red()
        self.data.rgbGreen = c.green()
        self.data.rgbBlue = c.blue()
        self.data.rgbAlpha = c.alpha()
    def addBrushStyleSelector(self):
        self.brushStyleL = self.createOneLineLabel(self.tr("Brush Style"))
        self.brushStyleW = BrushStyleSelector(self.contentW, QApplication.instance().brushStyleModel)
        self.brushStyleL.setBuddy(self.brushStyleW)
        self.addLabelWidgetPair(self.brushStyleL, self.brushStyleW)
        self.brushStyleW.currentDatasetChanged.connect(self.onBrushStyleChange)
    def onBrushStyleChange(self, s):
        self.data.brushStyle = s
