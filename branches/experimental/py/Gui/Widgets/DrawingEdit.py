from PyQt4.QtGui import *
from PyQt4.QtCore import *

from Gui.Canvas.CanvasScene import *
from Gui.Canvas.CanvasView import *

from Gui.ItemViews.PenItemView import *
from Gui.ItemViews.BrushItemView import *

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
        self.toolsW = QWidget(self)
        self.toolsW.setLayout(QVBoxLayout(self.toolsW))
        self.toolsW.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.setupToolsWidget()
        self.setupSettingsWidget()

        self.modeW = QLabel(self.tr("No Tool Selected"), self.toolsW)
        self.modeW.setAlignment(Qt.AlignBottom | Qt.AlignHCenter)
        
        self.toolsW.layout().addWidget(self.toolBoxW)
        self.toolsW.layout().addWidget(self.settingsW)
        self.toolsW.layout().addWidget(self.modeW)
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
        self.settingsW.setLayout(QVBoxLayout(self.settingsW))
        self.pensW = PenItemView(self.settingsW, QApplication.instance().penModel)
        self.brushesW = BrushItemView(self.settingsW, QApplication.instance().brushModel)
        self.settingsW.layout().addWidget(QLabel(self.tr("Pen"), self.settingsW))
        self.settingsW.layout().addWidget(self.pensW)
        self.settingsW.layout().addWidget(QLabel(self.tr("Brush"), self.settingsW))
        self.settingsW.layout().addWidget(self.brushesW)
#        self.pensW.currentDatasetChanged.connect(self.canvasS.onPenChange)
#        self.brushesW.currentDatasetChanged.connect(self.canvasS.onBrushChange)
    def setupToolsWidget(self):
        self.toolBoxW = QWidget(self.toolsW)
        self.toolBoxW.setLayout(QGridLayout(self.toolBoxW))
        self.straightLineW = QPushButton(self.tr("Straight Line"), self.toolBoxW)
        self.polygonLineW = QPushButton(self.tr("Polygon Line"), self.toolBoxW)
        self.rectangleW = QPushButton(self.tr("Rectangle"), self.toolBoxW)
        self.ellipseW = QPushButton(self.tr("Ellipse"), self.toolBoxW)
        self.pathW = QPushButton(self.tr("Path"), self.toolBoxW)
        self.deleteW = QPushButton(self.tr("Delete"), self.toolBoxW)
        self.editW = QPushButton(self.tr("Edit"), self.toolBoxW)
        self.moveW = QPushButton(self.tr("Move"), self.toolBoxW)
        self.moveW.setEnabled(False)

        self.toolBoxW.layout().addWidget(self.straightLineW, 0, 0)
        self.toolBoxW.layout().addWidget(self.polygonLineW, 0, 1)
        self.toolBoxW.layout().addWidget(self.rectangleW, 0, 2)
        self.toolBoxW.layout().addWidget(self.ellipseW, 1, 0)
        self.toolBoxW.layout().addWidget(self.pathW, 1, 1)
        self.toolBoxW.layout().addWidget(self.editW, 1, 2)
        self.toolBoxW.layout().addWidget(self.moveW, 2, 0)
        self.toolBoxW.layout().addWidget(self.deleteW, 2, 1)

        self.straightLineW.clicked.connect(self.onStraightLineRequest)
#        self.straightLineW.clicked.connect(self.canvasS.drawStraightLine)
        self.rectangleW.clicked.connect(self.onRectangleRequest)
#        self.rectangleW.clicked.connect(self.canvasS.drawRectangle)
        self.polygonLineW.clicked.connect(self.onPolygonLineRequest)
#        self.polygonLineW.clicked.connect(self.canvasS.drawPolygon)
        self.ellipseW.clicked.connect(self.onEllipseRequest)
#        self.ellipseW.clicked.connect(self.canvasS.drawEllipse)
        self.pathW.clicked.connect(self.onPathRequest)
#        self.pathW.clicked.connect(self.canvasS.drawPath)
        self.deleteW.clicked.connect(self.onDeleteRequest)
#        self.deleteW.clicked.connect(self.canvasS.onDelete)
        self.editW.clicked.connect(self.onEditRequest)
#        self.editW.clicked.connect(self.canvasS.onEdit)
        self.moveW.clicked.connect(self.onMoveRequest)
#        self.moveW.clicked.connect(self.canvasS.onMove)
    def setValue(self, drawing):
        self.drawing = drawing
