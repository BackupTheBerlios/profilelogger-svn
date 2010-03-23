from Gui.Dialogs.DatasetEditorDialog import *

from PyQt4.QtCore import *

from Gui.Widgets.ColorSelectionWidget import *
from Gui.Widgets.PixelInputWidget import *
from Gui.ItemViews.PenStyleSelector import *
from Gui.ItemViews.PenJoinStyleSelector import *
from Gui.ItemViews.PenCapStyleSelector import *
from Gui.ItemViews.BrushItemView import *

class PenEditorDialog(DatasetEditorDialog):
    def __init__(self, parent, data):
        DatasetEditorDialog.__init__(self, parent, data)
        self.addContentPanel(self.tr("Pen"))
        self.addIdDisplay()
        self.addNameEdit()
        self.addDisplay()
        self.addColorSelector()
        self.addWidthEdit()
        self.addPenCapStyleSelector()
        self.addPenJoinStyleSelector()
        self.addPenStyleSelector()
        self.addBrushSelector()
        self.addDescriptionEdit()
        self.addButtons()

        self.idW.setValue(self.data.id)
        self.nameW.setValue(unicode(self.data.name))
        self.colorW.setColor(self.data.getColor())
        self.penCapStyleW.setValue(self.data.penCapStyle)
        self.penJoinStyleW.setValue(self.data.penJoinStyle)
        self.penStyleW.setValue(self.data.penStyle)
        self.widthW.setValue(self.data.width)
        self.brushW.selectDataset(self.data.brush)
        self.descriptionW.setValue(unicode(self.data.description))
        
        self.nameW.nameChanged.connect(self.onNameChange)
        self.descriptionW.descriptionChanged.connect(self.onDescriptionChange)
    def onNameChange(self, txt):
        self.data.name = unicode(txt)
    def onDescriptionChange(self, txt):
        self.data.description = unicode(txt)
    def addColorSelector(self):
        self.colorL = self.createOneLineLabel(self.tr("Pen Color"))
        self.colorW = ColorSelectionWidget(self.contentW)
        self.colorL.setBuddy(self.colorW)
        self.addLabelWidgetPair(self.colorL, self.colorW)
        self.colorW.colorChanged.connect(self.onPenColorChange)
    def onPenColorChange(self, c):
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
    def addDisplay(self):
        self.previewS = QGraphicsScene(self)
        self.previewS.addLine(QLineF(0, 0, 100, 100))
        self.previewL = self.createMultiLineLabel(self.tr("Preview"))
        self.previewW = QGraphicsView(self.contentW)
        self.previewW.setRenderHints(QPainter.Antialiasing | QPainter.TextAntialiasing | QPainter.SmoothPixmapTransform | QPainter.HighQualityAntialiasing | QPainter.NonCosmeticDefaultPen)
        self.line = QGraphicsLineItem(None, self.previewS)
        self.line.setLine(QLineF(0, 0, 30, 30))
        self.line.setPen(QPen(Qt.black))
        self.addLabelWidgetPair(self.previewL, self.previewW)
    def addWidthEdit(self):
        self.widthL = self.createOneLineLabel(self.tr("Width"))
        self.widthW = PixelInputWidget(self.contentW)
        self.widthL.setBuddy(self.widthW)
        self.addLabelWidgetPair(self.widthL, self.widthW)
        self.widthW.valueChanged.connect(self.onWidthChange)
    def onWidthChange(self, v):
        self.data.width = v
    def addPenCapStyleSelector(self):
        self.penCapStyleL = self.createOneLineLabel(self.tr("Pen Cap Style"))
        self.penCapStyleW = PenCapStyleSelector(self.contentW, QApplication.instance().penCapStyleModel)
        self.penCapStyleL.setBuddy(self.penCapStyleW)
        self.addLabelWidgetPair(self.penCapStyleL, self.penCapStyleW)
        self.penCapStyleW.currentDatasetChanged.connect(self.onPenCapStyleChange)
    def onPenCapStyleChange(self, s):
        self.data.penCapStyle = s
    def addPenJoinStyleSelector(self):
        self.penJoinStyleL = self.createOneLineLabel(self.tr("Pen Join Style"))
        self.penJoinStyleW = PenJoinStyleSelector(self.contentW, QApplication.instance().penJoinStyleModel)
        self.penJoinStyleL.setBuddy(self.penJoinStyleW)
        self.addLabelWidgetPair(self.penJoinStyleL, self.penJoinStyleW)
        self.penJoinStyleW.currentDatasetChanged.connect(self.onPenJoinStyleChange)
    def onPenJoinStyleChange(self, s):
        self.data.penJoinStyle = s
    def addPenStyleSelector(self):
        self.penStyleL = self.createOneLineLabel(self.tr("Pen Style"))
        self.penStyleW = PenStyleSelector(self.contentW, QApplication.instance().penStyleModel)
        self.penStyleL.setBuddy(self.penStyleW)
        self.addLabelWidgetPair(self.penStyleL, self.penStyleW)
        self.penStyleW.currentDatasetChanged.connect(self.onPenStyleChange)
    def onPenStyleChange(self, s):
        self.data.penStyle = s
    def addBrushSelector(self):
        self.brushL = self.createMultiLineLabel(self.tr("Brush"))
        self.brushW = BrushItemView(self.contentW, QApplication.instance().brushModel)
        self.brushL.setBuddy(self.brushW)
        self.addLabelWidgetPair(self.brushL, self.brushW)
        self.brushW.currentDatasetChanged.connect(self.onBrushChange)
    def onBrushChange(self, b):
        self.data.brush = b
