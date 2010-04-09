from PyQt4.QtGui import *
from PyQt4.QtCore import *

from Gui.Dialogs.Dialog import Dialog

from Gui.Widgets.PixelInputWidget import *
from Gui.Widgets.ColorSelectionWidget import *
from Gui.Widgets.PenCapStyleSelector import *
from Gui.Widgets.PenJoinStyleSelector import *
from Gui.Widgets.PenStyleSelector import *
from Gui.Widgets.BrushStyleSelector import *

class CanvasItemEditorDialog(Dialog):
    def __init__(self, parent, itm):
        QDialog.__init__(self, parent)
        self.itm = itm
        self.setLayout(QVBoxLayout(self))
    def addContentWidget(self, title):
        self.contentW = QGroupBox(title, self)
        self.contentW.setLayout(QGridLayout(self.contentW))
        self.layout().addWidget(self.contentW)
        self.r = 0
        self.lC = 0
        self.wC = 1
    def addButtons(self):
        self.bbW = QDialogButtonBox(QDialogButtonBox.Save | QDialogButtonBox.Cancel, Qt.Horizontal, self)
        self.bbW.accepted.connect(self.accept)
        self.bbW.rejected.connect(self.reject)
        self.layout().addWidget(self.bbW)
    def addPenWidthEditor(self):
        self.penWidthW = PixelInputWidget(self.contentW)
        self.penWidthW.valueChanged.connect(self.onPenWidthChange)
        self.penWidth = self.itm.pen().width()
        self.penWidthW.setValue(self.penWidth)
        self.addLabelWidgetPair(self.tr("Pen Width:"), self.penWidthW)
    def onPenWidthChange(self, w):
        self.penWidth = w
    def addPenColorEditor(self):
        self.penColorW = ColorSelectionWidget(self.contentW)
        self.penColorW.colorChanged.connect(self.onPenColorChange)
        self.penColor = self.itm.pen().color()
        self.penColorW.setColor(self.penColor)
        self.addLabelWidgetPair(self.tr("Pen Color:"), self.penColorW)
    def onPenColorChange(self, c):
        self.penColor = c
    def addBrushColorEditor(self):
        self.brushColorW = ColorSelectionWidget(self.contentW)
        self.brushColorW.colorChanged.connect(self.onBrushColorChange)
        self.brushColor = self.itm.brush().color()
        self.brushColorW.setColor(self.brushColor)
        self.addLabelWidgetPair(self.tr("Brush Color:"), self.brushColorW)
    def onBrushColorChange(self, c):
        self.brushColor = c
    def addPenCapStyleEditor(self):
        self.penCapStyleW = PenCapStyleSelector(self.contentW)
        self.penCapStyleW.styleChanged.connect(self.onPenCapStyleChange)
        self.penCapStyle = self.itm.pen().capStyle()
        self.penCapStyleW.setPenCapStyle(self.penCapStyle)
        self.addLabelWidgetPair(self.tr("Pen Cap Style:"), self.penCapStyleW)
    def onPenCapStyleChange(self, s):
        self.penCapStyle = s
    def addPenJoinStyleEditor(self):
        self.penJoinStyleW = PenJoinStyleSelector(self.contentW)
        self.penJoinStyleW.styleChanged.connect(self.onPenJoinStyleChange)
        self.penJoinStyle = self.itm.pen().joinStyle()
        self.penJoinStyleW.setPenJoinStyle(self.penJoinStyle)
        self.addLabelWidgetPair(self.tr("Pen Join Style:"), self.penJoinStyleW)
    def onPenJoinStyleChange(self, s):
        self.penJoinStyle = s
    def addPenStyleEditor(self):
        self.penStyleW = PenStyleSelector(self.contentW)
        self.penStyleW.styleChanged.connect(self.onPenStyleChange)
        self.penStyle = self.itm.pen().style()
        self.penStyleW.setPenStyle(self.penStyle)
        self.addLabelWidgetPair(self.tr("Pen Style:"), self.penStyleW)
    def onPenStyleChange(self, s):
        self.penStyle = s
    def addBrushStyleEditor(self):
        self.brushStyleW = BrushStyleSelector(self.contentW)
        self.brushStyleW.styleChanged.connect(self.onBrushStyleChange)
        self.brushStyle = self.itm.brush().style()
        self.brushStyleW.setBrushStyle(self.brushStyle)
        self.addLabelWidgetPair(self.tr("Brush Style:"), self.brushStyleW)
    def onBrushStyleChange(self, s):
        self.brushStyle = s
    def addLabelWidgetPair(self, lblText, widget):
        self.contentW.layout().addWidget(QLabel(lblText, self.contentW), self.r, self.lC)
        self.contentW.layout().addWidget(widget, self.r, self.wC)
        self.r += 1
