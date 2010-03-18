from PyQt4.QtGui import *
from PyQt4.QtCore import *

from CanvasScene import *
from CanvasView import *

from Gui.Widgets.PixelInputWidget import PixelInputWidget
from Gui.Widgets.ColorSelectionWidget import ColorSelectionWidget

class CanvasWidget(QWidget):
    def __init__(self, parent):
        QWidget.__init__(self, parent)
        self.setLayout(QHBoxLayout(self))
        self.canvasS = CanvasScene(self)
        self.canvasV = CanvasView(self)
        self.canvasV.setScene(self.canvasS)
        self.configureTools()
        self.layout().addWidget(self.canvasV)
    def configureTools(self):
        self.toolsW = QGroupBox(self.tr("Tools"), self)
        self.toolsW.setLayout(QVBoxLayout(self.toolsW))

        self.straightLineW = QPushButton(self.tr("Straight Line"), self.toolsW)
        self.polygonLineW = QPushButton(self.tr("Polygon Line"), self.toolsW)
        self.rectangleW = QPushButton(self.tr("Rectangle"), self.toolsW)
        self.circleW = QPushButton(self.tr("Circle"), self.toolsW)
        self.ellipseW = QPushButton(self.tr("Ellipse"), self.toolsW)
        self.pathW = QPushButton(self.tr("Path"), self.toolsW)
        self.deleteW = QPushButton(self.tr("Delete"), self.toolsW)

        self.settingsW = QGroupBox(self.tr("Settings"), self.toolsW)
        self.settingsW.setLayout(QVBoxLayout(self.settingsW))
        self.penWidthW = PixelInputWidget(self.settingsW, self.tr("Pen Width:"))
        self.penWidthW.setValue(2)
        self.penColorW = ColorSelectionWidget(self.settingsW, self.tr("Pen Color"), Qt.black)
        self.settingsW.layout().addWidget(self.penWidthW)
        self.settingsW.layout().addWidget(self.penColorW)

        self.modeW = QLabel(self.tr("No Tool Selected"), self.toolsW)
        self.modeW.setAlignment(Qt.AlignBottom | Qt.AlignHCenter)
        
        self.toolsW.layout().addWidget(self.straightLineW)
        self.toolsW.layout().addWidget(self.polygonLineW)
        self.toolsW.layout().addWidget(self.rectangleW)
        self.toolsW.layout().addWidget(self.circleW)
        self.toolsW.layout().addWidget(self.ellipseW)
        self.toolsW.layout().addWidget(self.pathW)
        self.toolsW.layout().addWidget(self.deleteW)

        self.toolsW.layout().addWidget(self.settingsW)
        self.toolsW.layout().addWidget(self.modeW)
        
        self.layout().addWidget(self.toolsW)

        self.straightLineW.clicked.connect(self.onStraightLineRequest)
        self.straightLineW.clicked.connect(self.canvasS.drawStraightLine)
        self.polygonLineW.clicked.connect(self.onPolygonLineRequest)
        self.rectangleW.clicked.connect(self.onRectangleRequest)
        self.circleW.clicked.connect(self.onCircleRequest)
        self.ellipseW.clicked.connect(self.onEllipseRequest)
        self.pathW.clicked.connect(self.onPathRequest)
        self.deleteW.clicked.connect(self.onDeleteRequest)
        self.deleteW.clicked.connect(self.canvasS.onDelete)
        self.penWidthW.valueChanged.connect(self.canvasS.onPenWidthChange)
        self.penColorW.colorChanged.connect(self.canvasS.onPenColorChange)
    def onStraightLineRequest(self):
        self.modeW.setText(self.tr("Straight Line"))
    def onPolygonLineRequest(self):
        self.modeW.setText(self.tr("Polygon Line"))
    def onRectangleRequest(self):
        self.modeW.setText(self.tr("Rectangle"))
    def onCircleRequest(self):
        self.modeW.setText(self.tr("Circle"))
    def onEllipseRequest(self):
        self.modeW.setText(self.tr("Ellipse"))
    def onPathRequest(self):
        self.modeW.setText(self.tr("Path"))
    def onDeleteRequest(self):
        self.modeW.setText(self.tr("Delete"))
