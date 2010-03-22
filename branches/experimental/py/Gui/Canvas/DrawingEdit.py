from PyQt4.QtGui import *
from PyQt4.QtCore import *

from CanvasScene import *
from CanvasView import *

from Gui.Widgets.PixelInputWidget import PixelInputWidget
from Gui.Widgets.ColorSelectionWidget import ColorSelectionWidget
from Gui.Widgets.PenCapStyleSelector import PenCapStyleSelector
from Gui.Widgets.PenJoinStyleSelector import PenJoinStyleSelector
from Gui.Widgets.PenStyleSelector import PenStyleSelector
from Gui.Widgets.BrushStyleSelector import BrushStyleSelector

class DrawingEdit(QSplitter):
    def __init__(self, parent):
        QSplitter.__init__(self, parent)
        self.drawing = None
        self.setOrientation(Qt.Horizontal)
        self.canvasS = CanvasScene(self)
        self.canvasV = CanvasView(self)
        self.canvasV.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.canvasV.setScene(self.canvasS)
        self.configureTools()
        self.addWidget(self.toolsW)
        self.addWidget(self.canvasV)
    def configureTools(self):
        self.toolsW = QToolBox(self)
        self.toolsW.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.setupToolsWidget()
        self.setupSettingsWidget()

        self.modeW = QLabel(self.tr("No Tool Selected"), self.toolsW)
        self.modeW.setAlignment(Qt.AlignBottom | Qt.AlignHCenter)
        
        self.toolsW.addItem(self.toolBoxW, self.tr("Primitives"))
        self.toolsW.addItem(self.settingsW, self.tr("Pen \& Brush"))
        self.toolsW.addItem(self.modeW, self.tr("Hint"))
        
        self.penWidthW.valueChanged.connect(self.canvasS.onPenWidthChange)
        self.penColorW.colorChanged.connect(self.canvasS.onPenColorChange)
        self.brushColorW.colorChanged.connect(self.canvasS.onBrushColorChange)
        self.penCapStyleW.styleChanged.connect(self.canvasS.onPenCapStyleChange)
        self.penColorW.colorChanged.connect(self.penCapStyleW.onColorChange)
        self.penWidthW.valueChanged.connect(self.penCapStyleW.onPenWidthChange)
        self.penJoinStyleW.styleChanged.connect(self.canvasS.onPenJoinStyleChange)
        self.penColorW.colorChanged.connect(self.penJoinStyleW.onColorChange)
        self.penWidthW.valueChanged.connect(self.penJoinStyleW.onPenWidthChange)
        self.penStyleW.styleChanged.connect(self.canvasS.onPenStyleChange)
        self.penColorW.colorChanged.connect(self.penStyleW.onColorChange)
        self.penWidthW.valueChanged.connect(self.penStyleW.onPenWidthChange)
        self.brushStyleW.styleChanged.connect(self.canvasS.onBrushStyleChange)
        self.brushColorW.colorChanged.connect(self.brushStyleW.onColorChange)
        self.brushColorW.colorChanged.connect(self.canvasS.onBrushColorChange)

    def onStraightLineRequest(self):
        self.modeW.setText(self.tr("Straight Line"))
    def onPolygonLineRequest(self):
        self.modeW.setText(self.tr("Polygon Line"))
    def onRectangleRequest(self):
        self.modeW.setText(self.tr("Rectangle"))
    def onEllipseRequest(self):
        self.modeW.setText(self.tr("Ellipse"))
    def onPathRequest(self):
        self.modeW.setText(self.tr("Path"))
    def onDeleteRequest(self):
        self.modeW.setText(self.tr("Delete"))
    def onMoveRequest(self):
        self.modeW.setText(self.tr("Move"))
    def onEditRequest(self):
        self.modeW.setText(self.tr("Edit"))
    def setupSettingsWidget(self):
        self.settingsW = QWidget(self.toolsW)
        self.settingsW.setLayout(QGridLayout(self.settingsW))
        self.penWidthW = PixelInputWidget(self.settingsW, None)
        self.penWidthW.setValue(2)
        self.penColorW = ColorSelectionWidget(self.settingsW, None, Qt.black)
        self.penCapStyleW = PenCapStyleSelector(self.settingsW)

        self.brushColorW = ColorSelectionWidget(self.settingsW, None, Qt.black)
        self.penJoinStyleW = PenJoinStyleSelector(self.settingsW)
        self.penStyleW = PenStyleSelector(self.settingsW)
        self.brushStyleW = BrushStyleSelector(self.settingsW)

        r = 0
        lc = 0
        wc = 1
        self.settingsW.layout().addWidget(QLabel(self.tr("Pen Width"), self.settingsW), r, lc)
        self.settingsW.layout().addWidget(self.penWidthW, r, wc)
        r += 1
        self.settingsW.layout().addWidget(QLabel(self.tr("Pen Color"), self.settingsW), r, lc)
        self.settingsW.layout().addWidget(self.penColorW, r, wc)
        r += 1
        self.settingsW.layout().addWidget(QLabel(self.tr("Pen Cap Style"), self.settingsW), r, lc)
        self.settingsW.layout().addWidget(self.penCapStyleW, r, wc)
        r += 1
        self.settingsW.layout().addWidget(QLabel(self.tr("Pen Join Style"), self.settingsW), r, lc)
        self.settingsW.layout().addWidget(self.penJoinStyleW, r, wc)
        r += 1
        self.settingsW.layout().addWidget(QLabel(self.tr("Pen Line Style"), self.settingsW), r, lc)
        self.settingsW.layout().addWidget(self.penStyleW, r, wc)
        r += 1
        self.settingsW.layout().addWidget(QLabel(self.tr("Brush Color"), self.settingsW), r, lc)
        self.settingsW.layout().addWidget(self.brushColorW, r, wc)
        r += 1
        self.settingsW.layout().addWidget(QLabel(self.tr("Brush Style"), self.settingsW), r, lc)
        self.settingsW.layout().addWidget(self.brushStyleW, r, wc)
    def setupToolsWidget(self):
        self.toolBoxW = QWidget(self.toolsW)
        self.toolBoxW.setLayout(QVBoxLayout(self.toolBoxW))
        self.straightLineW = QPushButton(self.tr("Straight Line"), self.toolBoxW)
        self.polygonLineW = QPushButton(self.tr("Polygon Line"), self.toolBoxW)
        self.rectangleW = QPushButton(self.tr("Rectangle"), self.toolBoxW)
        self.ellipseW = QPushButton(self.tr("Ellipse"), self.toolBoxW)
        self.pathW = QPushButton(self.tr("Path"), self.toolBoxW)
        self.deleteW = QPushButton(self.tr("Delete"), self.toolBoxW)
        self.editW = QPushButton(self.tr("Edit"), self.toolBoxW)
        self.moveW = QPushButton(self.tr("Move"), self.toolBoxW)
        self.moveW.setEnabled(False)

        self.toolBoxW.layout().addWidget(self.straightLineW)
        self.toolBoxW.layout().addWidget(self.polygonLineW)
        self.toolBoxW.layout().addWidget(self.rectangleW)
        self.toolBoxW.layout().addWidget(self.ellipseW)
        self.toolBoxW.layout().addWidget(self.pathW)
        self.toolBoxW.layout().addWidget(self.editW)
        self.toolBoxW.layout().addWidget(self.moveW)
        self.toolBoxW.layout().addWidget(self.deleteW)

        self.straightLineW.clicked.connect(self.onStraightLineRequest)
        self.straightLineW.clicked.connect(self.canvasS.drawStraightLine)
        self.rectangleW.clicked.connect(self.onRectangleRequest)
        self.rectangleW.clicked.connect(self.canvasS.drawRectangle)
        self.polygonLineW.clicked.connect(self.onPolygonLineRequest)
        self.polygonLineW.clicked.connect(self.canvasS.drawPolygon)
        self.ellipseW.clicked.connect(self.onEllipseRequest)
        self.ellipseW.clicked.connect(self.canvasS.drawEllipse)
        self.pathW.clicked.connect(self.onPathRequest)
        self.pathW.clicked.connect(self.canvasS.drawPath)
        self.deleteW.clicked.connect(self.onDeleteRequest)
        self.deleteW.clicked.connect(self.canvasS.onDelete)
        self.editW.clicked.connect(self.onEditRequest)
        self.editW.clicked.connect(self.canvasS.onEdit)
        self.moveW.clicked.connect(self.onMoveRequest)
        self.moveW.clicked.connect(self.canvasS.onMove)
    def setValue(self, drawing):
        self.drawing = drawing
